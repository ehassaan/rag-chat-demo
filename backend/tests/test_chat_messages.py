from fastapi.testclient import TestClient
from app.main import app
from app.models.chat import ChatSession
from app.db.session import get_db_session
from sqlmodel import Session
from app.core.config import settings

client = TestClient(app, headers={"X-API-Key": settings.api_key})


def test_create_and_get_chat_message():

    db = next(get_db_session())

    chat_session = ChatSession(user_id=1, session_name="Test Session")
    db.add(chat_session)
    db.commit()
    db.refresh(chat_session)
    session_id = chat_session.session_id

    try:
        response = client.post(
            f"/api/v1/sessions/{session_id}/messages",
            json={"content": "Hello, World!", "role": "user"},
        )
        print(response.json())
        assert response.status_code == 201
        assert response.json()["content"] == "Hello, World!"

        # Get chat messages
        response = client.get(
            f"/api/v1/sessions/{session_id}/messages",
        )
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert response.json()[0]["content"] == "Hello, World!"
    except:
        raise
    finally:
        db.delete(chat_session)
        db.commit()
        db.close()
