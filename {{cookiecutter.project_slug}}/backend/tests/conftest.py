from typing import Generator

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
