import logging
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List
from app.models.chat import ChatMessage
from app.schemas.chat import ChatMessageCreate
from app.db.session import get_db_session

router = APIRouter()

@router.post("/sessions/{session_id}/messages", response_model=ChatMessage, status_code=201)
def create_message(
    session_id: int,
    message: ChatMessageCreate,
    session: Session = Depends(get_db_session),
):
    message.session_id = session_id
    db_message = ChatMessage.model_validate(message)
    session.add(db_message)
    session.commit()
    session.refresh(db_message)
    return db_message


@router.get("/sessions/{session_id}/messages", response_model=List[ChatMessage])
def read_messages(
    session_id: int,
    offset: int = 0,
    limit: int = 20,
    session: Session = Depends(get_db_session),
):
    limit = min(limit, 100)
    messages = session.exec(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.desc())
        .offset(offset)
        .limit(limit)
    ).all()
    return messages


@router.delete("/messages/{message_id}", response_model=ChatMessage)
def delete_message(
    message_id: int,
    session: Session = Depends(get_db_session),
):
    message = session.get(ChatMessage, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    session.delete(message)
    session.commit()
    return message
