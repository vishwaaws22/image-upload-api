from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_reports_the_upload_limit():
    response = client.get("/health")
    assert response.json()["max_upload_bytes"] == "5242880"
