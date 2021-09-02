from app.schemas.user import User, UserCreate, UserDB, UserUpdate
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from app.api import api_router
from app.models.user import user_db
from app.core.config import settings
from app.core.logger import logger


jwt_authentication = JWTAuthentication(
    secret=settings.SECRET_KEY,
    lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
)


def create_app():
    description = f"{settings.PROJECT_NAME} API"
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_PATH}/openapi.json",
        docs_url="/docs/",
        description=description,
        redoc_url=None,
    )
    fastapi_users = init_fastapi_users()
    setup_routers(app, fastapi_users)
    init_db_hooks(app)
    return app


def setup_routers(app: FastAPI, fastapi_users: FastAPIUsers) -> None:
    app.include_router(api_router, prefix=settings.API_PATH)
    app.include_router(
        fastapi_users.get_auth_router(
            jwt_authentication,
            requires_verification=True,
        ),
        prefix="/auth/jwt",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_register_router(),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_users_router(requires_verification=True),
        prefix="/users",
        tags=["users"],
    )


def init_fastapi_users() -> FastAPIUsers:
    fastapi_users = FastAPIUsers(
        user_db,
        [jwt_authentication],
        User,
        UserCreate,
        UserUpdate,
        UserDB,
    )
    return fastapi_users


def init_db_hooks(app: FastAPI) -> None:
    from app.db import database

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()


app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=5000)
