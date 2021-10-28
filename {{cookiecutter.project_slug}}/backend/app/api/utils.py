from typing import Any

from fastapi import APIRouter

from app.schemas.msg import Msg

router = APIRouter()


@router.get(
    "/hello-world",
    response_model=Msg,
    status_code=200,
    include_in_schema=False,
)
def test_hello_world() -> Any:
    return {"msg": "Hello world!"}
