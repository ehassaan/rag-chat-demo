from sqlmodel import create_engine, Session
from core.config import settings


engine = create_engine(settings.database_url, echo=True)

def get_db_session():
    with Session(engine) as session:
        yield session
