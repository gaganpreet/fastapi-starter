import uuid
from typing import Callable, Generator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker
from starlette.testclient import TestClient

from app.core.config import settings
from app.deps.users import get_user_manager
from app.factory import create_app
from app.models.item import Item
from app.models.user import User
from tests.utils import generate_random_string

engine = create_async_engine(
    settings.DATABASE_URL,
)
async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@pytest.fixture(scope="session")
async def db():
    async with async_session_maker() as session:
        yield session
        await session.rollback()
        await session.close()


@pytest.fixture(scope="session")
def default_password():
    return generate_random_string(32)


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def client(app) -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function", autouse=True)
async def auto_rollback(db: AsyncSession):
    await db.rollback()


@pytest.fixture(scope="session")
def create_user(db: AsyncSession, default_password: str):
    user_manager = next(get_user_manager())

    async def inner():
        user = User(
            id=uuid.uuid4(),
            email=f"{generate_random_string(20)}@{generate_random_string(10)}.com",
            hashed_password=user_manager.password_helper.hash(default_password),
        )
        db.add(user)
        await db.commit()
        return user

    return inner


@pytest.fixture(scope="session")
def create_item(db: AsyncSession, create_user: Callable):
    async def inner(user=None):
        if not user:
            user = await create_user()
        item = Item(
            user=user,
            value="value",
        )
        db.add(item)
        await db.commit()
        return item

    return inner
