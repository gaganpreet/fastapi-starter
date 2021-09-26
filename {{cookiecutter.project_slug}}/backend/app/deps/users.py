from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.manager import BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.core.config import settings
from app.db import database
from app.models.user import User as UserModel
from app.schemas.user import User, UserCreate, UserDB, UserUpdate

jwt_authentication: JWTAuthentication = JWTAuthentication(
    secret=settings.SECRET_KEY,
    lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
)


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, UserModel.__table__)


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
