from fastapi import APIRouter
from app.api import utils
from app.api import users

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(users.router, tags=["users"])
