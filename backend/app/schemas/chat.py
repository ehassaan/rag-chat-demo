from pydantic import BaseModel, Field
from typing import List, Optional
from sqlmodel import SQLModel

class ChatSessionCreate(SQLModel):
    session_name: str = Field(description="Name of the chat session")
    is_favorite: bool = Field(False, description="Marks session as favorite")

class ChatSessionPatch(SQLModel):
    session_name: Optional[str] = Field(None, description="Name of the chat session")
    is_favorite: Optional[bool] = Field(False, description="Marks session as favorite")

class ChatMessageCreate(SQLModel):
    session_id: Optional[int] = Field(description="ID of the chat session this message belongs to")
    content: str = Field(description="Content of the chat message")
    role: str = Field("user", description="Role of the message sender (e.g., 'user', 'assistant')")
