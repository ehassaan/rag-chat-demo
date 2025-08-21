from fastapi.testclient import TestClient
from app.main import app
from app.models.chat import ChatSession
from sqlalchemy.orm import Session
from app.db.session import get_db_session
from app.core.config import settings

client = TestClient(app, headers={
    "X-API-Key": settings.api_key
})

def test_create_chat_session():
    response = client.post("/api/v1/sessions/", json={"user_id": 1, "session_name": "Test Session", "session_id": 1})
    res = response.json()
    assert response.status_code == 201
    assert res["session_name"] == "Test Session"

def test_get_chat_session():
    response = client.get("/api/v1/sessions/1")
    assert response.status_code == 200
    assert response.json()["session_name"] == "Test Session"

def test_update_chat_session():
    response = client.put("/api/v1/sessions/1", json={"session_name": "Updated Session"})
    assert response.status_code == 200
    assert response.json()["session_name"] == "Updated Session"

def test_delete_chat_session():
    response = client.delete("/api/v1/sessions/1")
    assert response.status_code == 200
    response = client.get("/api/v1/sessions/1")
    assert response.status_code == 404

def test_get_all_chat_sessions():
    response = client.get("/api/v1/sessions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list

def test_create_chat_session_invalid_data():
    response = client.post("/api/v1/sessions/", json={"user_id": "invalid", "session_name": ""})
    assert response.status_code == 422  # Unprocessable Entity for invalid data
