from fastapi.testclient import TestClient
from src.main import app
from src.models.chat import ChatSession
from sqlalchemy.orm import Session
from src.db.session import get_session

client = TestClient(app)

def test_create_chat_session():
    response = client.post("/api/v1/chat_sessions/", json={"user_id": 1, "session_name": "Test Session"})
    assert response.status_code == 201
    assert response.json()["session_name"] == "Test Session"

def test_get_chat_session():
    response = client.get("/api/v1/chat_sessions/1")
    assert response.status_code == 200
    assert response.json()["session_name"] == "Test Session"

def test_update_chat_session():
    response = client.put("/api/v1/chat_sessions/1", json={"session_name": "Updated Session"})
    assert response.status_code == 200
    assert response.json()["session_name"] == "Updated Session"

def test_delete_chat_session():
    response = client.delete("/api/v1/chat_sessions/1")
    assert response.status_code == 204
    response = client.get("/api/v1/chat_sessions/1")
    assert response.status_code == 404

def test_get_all_chat_sessions():
    response = client.get("/api/v1/chat_sessions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list

def test_create_chat_session_invalid_data():
    response = client.post("/api/v1/chat_sessions/", json={"user_id": "invalid", "session_name": ""})
    assert response.status_code == 422  # Unprocessable Entity for invalid data