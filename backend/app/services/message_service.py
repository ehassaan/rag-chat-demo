import logging
from fastapi import HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from app.models.chat import ChatMessage
from app.schemas.chat import ChatMessageCreate

logger = logging.getLogger(__name__)


def create_message(
    session_id: int,
    message: ChatMessageCreate,
    db: Session,
) -> ChatMessage:
    
    print("=======---------------------Creating Message: ", session_id, message)
    try:
        message.session_id = session_id
        db_message = ChatMessage.model_validate(message)
        print("=======---------------------Validated Message: ", session_id, db_message)
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
    except Exception as e:
        logger.error(f"Error creating message: {e}")
        raise e
    return db_message


def read_messages(
    session_id: int,
    offset: int = 0,
    limit: int = 20,
    db: Session = None,
) -> List[ChatMessage]:

    limit = min(limit, 100)
    statement = (
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    messages = db.exec(statement).all()
    return messages


def delete_message_service(
    message_id: int,
    db: Session,
) -> Optional[ChatMessage]:
    message = db.get(ChatMessage, message_id)
    if not message:
        return HTTPException(status_code=404, detail="Message not found")
    db.delete(message)
    db.commit()