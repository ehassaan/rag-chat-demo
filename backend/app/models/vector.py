from pydantic import ConfigDict
from sqlmodel import SQLModel, Field, Relationship
from pgvector.sqlalchemy import Vector
from typing import Any, Optional, List
from app.core.config import settings
from app.models.base_model import BaseModel
from app.models.chat import ChatSession


class DocumentIndex(BaseModel, table=True):
    id: int = Field(primary_key=True)
    session_id: int = Field(foreign_key="chatsession.session_id")
    document_id: str = Field(description="ID of the document")
    chunk_text: str = Field(description="Content of the document")
    chunk_index: int = Field(description="Index of the chunk within the document")
    chunk_embedding: Any = Field(sa_type=Vector(settings.pgvector_dimension))
    chunk_type: Optional[str] = Field(
        "text", description="Type of the document (e.g., 'text', 'image', 'video')"
    )

    session: ChatSession = Relationship(back_populates="document_chunks")
