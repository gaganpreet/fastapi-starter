from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String


class Item(DeclarativeBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    user_id = Column(GUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="items")

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    value = Column(String)
