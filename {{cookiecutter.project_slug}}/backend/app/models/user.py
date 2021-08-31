from app.db import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql.functions import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"
