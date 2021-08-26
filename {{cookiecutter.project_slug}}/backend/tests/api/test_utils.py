from fastapi.testclient import TestClient

from app.core.config import settings


def test_hello_world(client: TestClient) -> None:
    resp = client.get(f"{settings.API_PATH}/hello-world")
    data = resp.json()
    assert data["msg"] == "Hello world!"
