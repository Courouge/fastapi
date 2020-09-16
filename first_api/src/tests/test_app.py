from starlette.testclient import TestClient

from app.main import app
import base64

version = "0.0.0"

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_auth():
    valid_credentials = base64.b64encode(b"admin:admin").decode("utf-8")
    # curl -X POST "http://127.0.0.1/token" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "grant_type=&username=test&password=test&scope=&client_id=&client_secret="
    response = client.get(
        "/token",
        headers={"Authorization": "Basic " + valid_credentials }
    )
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
