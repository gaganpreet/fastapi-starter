from httpx import AsyncClient

from app.core.config import settings
from app.models.item import Item
from app.models.user import User
from tests.utils import get_jwt_header


class TestGetItems:
    async def test_get_items_not_logged_in(self, client: AsyncClient):
        resp = await client.get(settings.API_PATH + "/items")
        assert resp.status_code == 401

    async def test_get_items(self, client: AsyncClient, create_user, create_item):
        user: User = await create_user()
        await create_item(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(settings.API_PATH + "/items", headers=jwt_header)
        assert resp.status_code == 200
        assert resp.headers["Content-Range"] == "0-1/1"
        assert len(resp.json()) == 1


class TestGetSingleItem:
    async def test_get_single_item(self, client: AsyncClient, create_user, create_item):
        user: User = await create_user()
        item: Item = await create_item(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(
            settings.API_PATH + f"/items/{item.id}", headers=jwt_header
        )
        assert resp.status_code == 200, resp.text
        data = resp.json()
        assert data["id"] == item.id
        assert data["value"] == item.value


class TestCreateItem:
    async def test_create_item(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.post(
            settings.API_PATH + "/items", headers=jwt_header, json={"value": "value"}
        )
        assert resp.status_code == 201, resp.text
        assert resp.json()["id"]


class TestDeleteItem:
    async def test_delete_item(self, client: AsyncClient, create_user, create_item):
        user: User = await create_user()
        item: Item = await create_item(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/items/{item.id}", headers=jwt_header
        )
        assert resp.status_code == 200

    async def test_delete_item_does_not_exist(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/items/{10**6}", headers=jwt_header
        )
        assert resp.status_code == 404, resp.text


class TestUpdateItem:
    async def test_update_item(self, client: AsyncClient, create_user, create_item):
        user: User = await create_user()
        item: Item = await create_item(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.put(
            settings.API_PATH + f"/items/{item.id}",
            headers=jwt_header,
            json={"value": "new value"},
        )
        assert resp.status_code == 200, resp.text
        assert resp.json()["value"] == "new value"
