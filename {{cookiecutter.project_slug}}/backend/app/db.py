from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import registry

engine = create_engine(settings.DATABASE_URL, echo=True, future=True)

mapper_registry = registry()
Base = mapper_registry.generate_base()
