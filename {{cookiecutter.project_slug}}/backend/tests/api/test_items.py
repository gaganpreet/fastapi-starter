from sqlalchemy.orm.session import Session
from starlette.testclient import TestClient

from app.core.config import settings
from app.models.item import Item
from app.models.user import User
from tests.utils import get_jwt_header


class TestGetItems:
    def test_get_items_not_logged_in(self, client: TestClient):
        resp = client.get(settings.API_PATH + "/items")
        assert resp.status_code == 401

    def test_get_items(self, db: Session, client: TestClient, create_user, create_item):
        user: User = create_user()
        create_item(user=user)
        jwt_header = get_jwt_header(user)
        resp = client.get(settings.API_PATH + "/items", headers=jwt_header)
        assert resp.status_code == 200
        assert resp.headers["Content-Range"] == "0-1/1"
        assert len(resp.json()) == 1
