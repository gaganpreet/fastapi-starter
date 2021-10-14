import random
import string
from typing import Any

from fastapi_users.jwt import generate_jwt

from app.deps.users import jwt_authentication
from app.models.user import User


def generate_random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def get_jwt_header(user: User) -> Any:
    data = {"user_id": str(user.id), "aud": jwt_authentication.token_audience}
    token = generate_jwt(
        data, jwt_authentication.secret, jwt_authentication.lifetime_seconds
    )
    return {"Authorization": f"Bearer {token}"}
