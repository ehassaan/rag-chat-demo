import datetime as dt
from sqlmodel import SQLModel, Field

class BaseModel(SQLModel):
    created_at: dt.datetime = Field(default_factory=dt.datetime.now, description="Timestamp when the session was created")
    updated_at: dt.datetime = Field(default_factory=dt.datetime.now, description="Timestamp when the session was last updated")
