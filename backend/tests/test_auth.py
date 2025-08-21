from fastapi.testclient import TestClient
from app.core.config import settings
from app.main import app


client = TestClient(app)
API_KEY_NAME = "X-API-Key"


def test_get_api_key_valid():
    valid_api_key = settings.api_key
    response = client.get("/api/v1/sessions", headers={API_KEY_NAME: valid_api_key})
    assert response.status_code == 200


def test_get_api_key_invalid():
    invalid_api_key = "invalid_api_key"
    response = client.get("/api/v1/sessions", headers={API_KEY_NAME: invalid_api_key})
    assert response.status_code == 403
