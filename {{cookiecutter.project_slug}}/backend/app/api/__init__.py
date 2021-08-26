from fastapi import APIRouter
from app.api import utils

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
