from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

from app.core.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True, future=True)
_Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

mapper_registry = registry()
Base = mapper_registry.generate_base()


def get_db() -> Generator:
    db = None
    try:
        db = _Session(future=True)
        yield db
    finally:
        if db is not None:
            db.close()
