from fastapi.testclient import TestClient
from src.main import app
from src.models.chat import ChatSession, ChatMessage
from src.db.session import get_session
from sqlmodel import Session

client = TestClient(app)

def test_create_chat_message():
    with get_session() as session:  # type: Session
        session.add(ChatSession(user_id=1, session_name="Test Session"))
        session.commit()
        session.refresh(session)

    response = client.post(
        f"/api/v1/chat_sessions/{session.session_id}/messages",
        json={"content": "Hello, World!", "timestamp": "2023-10-01T12:00:00Z"}
    )
    assert response.status_code == 201
    assert response.json()["content"] == "Hello, World!"

def test_get_chat_messages():
    with get_session() as session:  # type: Session
        session.add(ChatMessage(session_id=1, content="Hello, World!", timestamp="2023-10-01T12:00:00Z"))
        session.commit()

    response = client.get(f"/api/v1/chat_sessions/1/messages")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["content"] == "Hello, World!"