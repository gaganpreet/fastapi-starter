from typing import Any, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession
from starlette.responses import Response
from typing import Annotated

from app.deps.db import get_async_session
from app.deps.users import current_superuser
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter()
CurrentAsyncSession = Annotated[AsyncSession, Depends(get_async_session)]
CurrentSuperuser = Annotated[User, Depends(current_superuser)]


@router.get("/users", response_model=List[UserRead])
async def get_users(
    response: Response,
    session: CurrentAsyncSession,
    user: CurrentSuperuser,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    total = await session.scalar(select(func.count(User.id)))
    users = (
        (await session.execute(select(User).offset(skip).limit(limit))).scalars().all()
    )
    response.headers["Content-Range"] = f"{skip}-{skip + len(users)}/{total}"
    return users
