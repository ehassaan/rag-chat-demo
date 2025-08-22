from fastapi import APIRouter, HTTPException, Depends, Response
from sqlmodel import Session, select
from typing import List
from app.models.chat import ChatSession
from app.db.session import get_db_session
from app.schemas.chat import ChatSessionCreate, ChatSessionPatch

router = APIRouter()


@router.post("/", response_model=ChatSession, status_code=201)
async def create_chat_session(
    data: ChatSessionCreate,
    db: Session = Depends(get_db_session),
):
    model = ChatSession.model_validate(data)
    db.add(model)
    db.commit()
    db.refresh(model) # Refresh to get the ID and other defaults set by the database
    return model


@router.get("/", response_model=List[ChatSession])
async def read_chat_sessions(
    skip: int = 0,
    limit: int = 20,
    db=Depends(get_db_session),
):
    limit = min(limit, 100)
    sessions = db.exec(select(ChatSession).offset(skip).limit(limit)).all()
    return sessions


@router.get("/{session_id}", response_model=ChatSession)
async def read_chat_session(
    session_id: int,
    db: Session = Depends(get_db_session),
):
    session = db.get(ChatSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    return session


@router.patch("/{session_id}", response_model=ChatSession)
async def update_chat_session(
    session_id: int,
    session: ChatSessionPatch,
    db: Session = Depends(get_db_session),
):
    db_session = db.get(ChatSession, session_id)
    if not db_session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    db_session.sqlmodel_update(session.model_dump(exclude_unset=True))
    db.commit()
    db.refresh(db_session)
    return db_session


@router.delete("/{session_id}", response_model=dict)
async def delete_chat_session(
    session_id: int,
    db: Session = Depends(get_db_session),
):
    session = db.get(ChatSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    db.delete(session)
    db.commit()
    return {"detail": "Chat session deleted"}
