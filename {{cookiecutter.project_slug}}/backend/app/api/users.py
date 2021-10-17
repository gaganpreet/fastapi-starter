from typing import Any, List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy import func, select
from sqlalchemy.orm.session import Session
from starlette.responses import Response

from app.deps.db import get_db
from app.deps.users import current_superuser
from app.models.user import User
from app.schemas.user import User as UserSchema

router = APIRouter()


@router.get("/users/", response_model=List[UserSchema])
def get_users(
    response: Response,
    db: Session = Depends(get_db),
    user: User = Depends(current_superuser),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    total = db.scalar(select(func.count(User.id)))
    users = db.execute(select(User).offset(skip).limit(limit)).scalars().all()
    response.headers["Content-Range"] = f"{skip}-{skip + len(users)}/{total}"
    return users
