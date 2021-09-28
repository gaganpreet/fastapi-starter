from fastapi import APIRouter

from app.api import users, utils
from app.api.crud import item

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(item.router)
