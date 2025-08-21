from fastapi.testclient import TestClient
from fastapi.security import APIKeyHeader
from src.main import app


client = TestClient(app)

# @app.get("/test-auth")
# def test_auth(api_key: str = Depends(get_api_key)):
#     return {"message": "API key is valid!"}

def test_get_api_key_valid():
    # Simulate a valid API key
    valid_api_key = "your_valid_api_key"
    response = client.get("/test-auth", headers={API_KEY_NAME: valid_api_key})
    assert response.status_code == 200
    assert response.json() == {"message": "API key is valid!"}

def test_get_api_key_invalid():
    # Simulate an invalid API key
    invalid_api_key = "invalid_api_key"
    response = client.get("/test-auth", headers={API_KEY_NAME: invalid_api_key})
    assert response.status_code == 403
    assert response.json() == {"detail": "Could not validate API key"}