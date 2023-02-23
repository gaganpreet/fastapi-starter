from typing import AsyncGenerator

from sqlalchemy.ext.asyncio.session import AsyncSession

from app.db import async_session_maker


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
        await session.close()
