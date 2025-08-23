from app.core.config import settings
from pydantic import RootModel
import cohere
from sqlmodel import Session, select, func
from app.models.vector import DocumentIndex
from app.models.chat import ChatMessage
from app.schemas.rag import DocumentChunk, GenerationMessage, GenerationDocument
from . import chunking_service
from fastapi import HTTPException
from . import message_service


client = cohere.ClientV2(settings.cohere_api_key)


def index_document(doc_id: str, text: str, session_id: str, db: Session):
    if db.exec(
        select(DocumentIndex).where(DocumentIndex.document_id == doc_id)
    ).first():
        raise HTTPException(400, "Document already indexed")

    chunks = chunking_service.create_document_chunks(text)
    response = client.embed(
        texts=[c.text for c in chunks],
        output_dimension=settings.pgvector_dimension,
        input_type="search_document",
        embedding_types=["float"],
        model=settings.embedding_model,
    )
    embedding = response.embeddings.float_[0]
    for i, chunk in enumerate(chunks):
        doc = DocumentIndex(
            document_id=doc_id,
            session_id=session_id,
            chunk_text=chunk.text,
            chunk_index=i,
            chunk_type="text",
            chunk_embedding=embedding,
        )
        db.add(doc)
    db.commit()


def generate_response(
    *,
    messages: list[GenerationMessage],
    documents: list[GenerationDocument],
    session_id: int,
):
    response = client.chat(
        model=settings.generation_model,
        documents=documents,
        messages=messages,
        max_tokens=settings.max_response_tokens,
    )
    text = response.message.content[0].text
    serialized = RootModel[list[GenerationDocument]](documents).model_dump_json()
    msg = ChatMessage(
        session_id=session_id,
        content=text,
        role="assistant",
        context=serialized,
    )
    return msg


def retrieve_similar_chunks(*, query: str, limit: int, session_id: int, db: Session):
    embedding = client.embed(
        texts=[query],
        output_dimension=settings.pgvector_dimension,
        input_type="search_query",
        embedding_types=["float"],
        model=settings.embedding_model,
    ).embeddings.float_[0]
    chunks = db.exec(
        select(
            DocumentIndex,
            DocumentIndex.chunk_embedding.l2_distance(embedding).label("l2_distance"),
        )
        .order_by(DocumentIndex.chunk_embedding.l2_distance(embedding))
        .where(
            (DocumentIndex.chunk_embedding.l2_distance(embedding) < 1.5)
            & (DocumentIndex.session_id == session_id)
        )
        .limit(limit)
    ).all()
    res_chunks = []
    for chunk, distance in chunks:
        chunk.chunk_embedding = chunk.chunk_embedding.tolist()
        chunk = DocumentChunk.model_validate(
            chunk.model_dump() | {"distance": distance}
        )
        res_chunks.append(chunk)
    return res_chunks


def chat(query: str, session_id: int, db: Session):
    similar_chunks = retrieve_similar_chunks(
        query=query, session_id=session_id, limit=5, db=db
    )
    new_message = ChatMessage(content=query, role="user", session_id=session_id)
    messages = message_service.read_messages(session_id, limit=5, db=db)
    messages.append(new_message)

    messages = [{"content": m.content, "role": m.role} for m in messages]
    documents = [
        {"data": d.chunk_text, "id": f"{d.document_id}_{d.id}"} for d in similar_chunks
    ]

    response = generate_response(
        messages=messages, documents=documents, session_id=session_id
    )
    print("--------GENERATED RESPONSE: ", session_id, response)
    message_service.create_message(session_id, new_message, db)
    res_msg = message_service.create_message(session_id, response, db)
    return res_msg
