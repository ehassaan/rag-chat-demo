import datetime as dt
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class ChatSession(SQLModel, table=True):
    session_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(1, description="ID of the user who owns the session")
    session_name: str
    is_favorite: bool = Field(default=False)
    messages: List["ChatMessage"] = Relationship(back_populates="session", cascade_delete=True)


class ChatMessage(SQLModel, table=True):
    message_id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="chatsession.session_id")
    content: str = Field(description="Content of the chat message")
    timestamp: str = Field(default_factory=lambda: dt.datetime.now().isoformat())
    session: ChatSession = Relationship(back_populates="messages")
