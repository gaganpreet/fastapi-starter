from typing import Any

from pydantic.main import BaseModel


class RequestParams(BaseModel):
    skip: int
    limit: int
    order_by: Any
