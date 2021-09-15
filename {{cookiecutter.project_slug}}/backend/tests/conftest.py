from typing import Generator

import pytest
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from starlette.testclient import TestClient

from app.core.config import settings
from app.db import Base
from app.deps.db import get_db
from app.factory import create_app

engine = create_engine(
    settings.TEST_DATABASE_URL,
    echo=True,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def client(app) -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def db() -> Generator:
    session = TestingSessionLocal()

    yield session

    session.rollback()
    session.commit()


@pytest.fixture(scope="session", autouse=True)
def override_get_db(app):
    db = None
    try:
        db = TestingSessionLocal()
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        if db:
            db.close()
    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function", autouse=True)
def auto_rollback(db):
    db.rollback()
