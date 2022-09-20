from typing import AsyncGenerator, Generator

from sqlalchemy.ext.asyncio.session import AsyncSession

from app.db import SessionLocal, async_session_maker


def get_db() -> Generator:
    db = None
    try:
        db = SessionLocal(future=True)
        yield db
    finally:
        if db is not None:
            db.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
        await session.close()
