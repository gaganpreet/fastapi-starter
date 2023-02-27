from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import func

from app.db import Base

if TYPE_CHECKING:
    from app.models.item import Item  # noqa: F401


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    items: Mapped["Item"] = relationship(back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"
