from sqlmodel import SQLModel, Field
from pgvector.sqlalchemy import Vector

class ChatMessageVector(SQLModel, table=True):
    message_id: int = Field(primary_key=True)
    vector: Vector(1536)  # Adjust the dimension based on your model
    session_id: int = Field(foreign_key="chatsession.session_id")