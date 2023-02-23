from httpx import AsyncClient

from app.core.config import settings


async def test_hello_world(client: AsyncClient) -> None:
    resp = await client.get(f"{settings.API_PATH}/hello-world")
    data = resp.json()
    assert data["msg"] == "Hello world!"
