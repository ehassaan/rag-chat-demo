from pydantic import BaseModel, Field
from typing import List, Optional
from sqlmodel import SQLModel
from pydantic import ConfigDict
import datetime as dt


class DocumentIndexCreateReq(SQLModel):
    session_id: int = Field(description="ID of the chat session")
    document_name: str = Field(description="Name of the chat session")
    document_content: str = Field(description="Content of the chat message")


# class GenerateReq(SQLModel):
#     prompt: str = Field(description="Prompt to generate response")
#     session_id: int = Field(description="ID of the chat session")


class DocumentChunk(SQLModel):
    id: int = Field(primary_key=True, description="ID of the document chunk")
    document_id: str = Field(description="ID of the document")
    distance: float = Field(description="Similarity score")
    chunk_text: str = Field(description="Content of the document")
    created_at: dt.datetime = Field(default_factory=dt.datetime.now)
    updated_at: dt.datetime = Field(default_factory=dt.datetime.now)

    model_config = ConfigDict(extra="ignore")


class GenerationMessage(SQLModel):
    content: str = Field(description="Content of the chat message")
    role: str = Field(description="Role of the message sender (e.g., 'user', 'assistant')")

class GenerationDocument(SQLModel):
    id: Optional[str] = Field(None, description="ID of the document")
    data: str = Field(description="Content of the document")

class GenerationRequest(SQLModel):
    messages: list[GenerationMessage] = Field(description="List of chat messages")
    documents: list[GenerationDocument] = Field(description="List of documents")
    session_id: int = Field(description="ID of the chat session")

