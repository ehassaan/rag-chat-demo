import datetime as dt
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from app.core.config import settings
from app.models.base_model import BaseModel


class ChatSession(BaseModel, table=True):
    session_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(1, description="ID of the user who owns the session")
    session_name: str
    is_favorite: bool = Field(default=False)
    # messages: List["ChatMessage"] = Relationship(cascade_delete=True)
    # document_chunks: List["DocumentIndex"] = Relationship(
    #     back_populates="session", cascade_delete=True
    # )


class ChatMessage(BaseModel, table=True):
    message_id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="chatsession.session_id", ondelete="CASCADE")
    role: str = Field(
        "user", description="Role of the message sender (e.g., 'user', 'assistant')"
    )
    content: str = Field(description="Content of the chat message")
    context: Optional[str] = Field(None, description="Context for the message, if any")
    # session: ChatSession = Relationship(back_populates="messages")
