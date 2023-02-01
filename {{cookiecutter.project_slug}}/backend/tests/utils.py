import secrets
import string
from typing import Any

from fastapi_users.jwt import generate_jwt

from app.deps.users import get_jwt_strategy
from app.models.user import User


def generate_random_string(length: int) -> str:
    return "".join(secrets.choice(string.ascii_lowercase) for i in range(length))


def get_jwt_header(user: User) -> Any:
    jwt_strategy = get_jwt_strategy()
    data = {"sub": str(user.id), "aud": jwt_strategy.token_audience}
    token = generate_jwt(data, jwt_strategy.secret, jwt_strategy.lifetime_seconds)
    return {"Authorization": f"Bearer {token}"}
