from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func

from app.db import Base, database
from app.schemas.user import UserDB


class User(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"


users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)
