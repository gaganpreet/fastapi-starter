import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base: DeclarativeMeta = declarative_base()

database = databases.Database(settings.DATABASE_URL)
