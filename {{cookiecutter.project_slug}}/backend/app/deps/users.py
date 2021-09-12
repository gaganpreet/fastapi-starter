from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from app.core.config import settings
from app.models.user import user_db
from app.schemas.user import User, UserCreate, UserDB, UserUpdate

jwt_authentication = JWTAuthentication(
    secret=settings.SECRET_KEY,
    lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
