import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import registry, sessionmaker

from app.core.config import settings

async_engine = create_async_engine(settings.ASYNC_DATABASE_URL)
async_session_maker = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# We still have a second old style sync SQLAlchemy engine for shell and alembic
engine = create_engine(settings.DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

mapper_registry = registry()
Base: DeclarativeMeta = declarative_base()

database = databases.Database(settings.DATABASE_URL)
