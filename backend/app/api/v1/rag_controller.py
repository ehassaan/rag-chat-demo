from fastapi import APIRouter, HTTPException, Depends, Response
from sqlmodel import Session, select
from typing import List, Any
from app.db.session import get_db_session
from app.services import rag_service
from app.schemas.rag import DocumentIndexCreateReq
from app.models.chat import ChatMessage
from app.schemas.rag import DocumentChunk, GenerationRequest, GenerationMessage

router = APIRouter()


@router.post("/index", response_model=dict, status_code=200)
async def index_document(
    data: DocumentIndexCreateReq,
    db: Session = Depends(get_db_session),
):
    rag_service.index_document(
        data.document_name, data.document_content, data.session_id, db
    )
    return {"message": "Document indexed successfully"}


@router.get("/search", response_model=List[DocumentChunk])
async def read_chat_sessions(
    query: str,
    session_id: int,
    limit: int = 5,
    db=Depends(get_db_session),
):
    if not query:
        raise HTTPException(
            status_code=400, detail="Query parameteer 'query' is required"
        )
    limit = min(limit, 50)
    chunks = rag_service.retrieve_similar_chunks(query=query, limit=limit, session_id=session_id, db=db)
    return chunks


@router.post("/generate", response_model=ChatMessage)
async def generate_response(data: GenerationRequest):
    response = rag_service.generate_response(
        messages=data.messages, documents=data.documents, session_id=data.session_id
    )
    return response


@router.post("/chat", response_model=ChatMessage)
async def chat(
    data: GenerationMessage,
    db=Depends(get_db_session),
):
    response = rag_service.chat(data.content, data.session_id, db)
    return response
