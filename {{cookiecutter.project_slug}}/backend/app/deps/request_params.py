import json
from typing import Annotated, Callable, Optional, Type

from fastapi import Depends, HTTPException, Query
from sqlalchemy import UnaryExpression, asc, desc

from app.db import Base
from app.models.item import Item
from app.schemas.request_params import RequestParams


def parse_react_admin_params(model: Type[Base]) -> Callable:
    """Parses sort and range parameters coming from a react-admin request"""

    def inner(
        sort_: Optional[str] = Query(
            None,
            alias="sort",
            description='Format: `["field_name", "direction"]`',
            example='["id", "ASC"]',
        ),
        range_: Optional[str] = Query(
            None,
            alias="range",
            description="Format: `[start, end]`",
            example="[0, 10]",
        ),
    ) -> RequestParams:
        skip, limit = 0, 10
        if range_:
            start, end = json.loads(range_)
            skip, limit = start, (end - start + 1)

        order_by: UnaryExpression = desc(model.id)
        if sort_:
            sort_column, sort_order = json.loads(sort_)
            if sort_order.lower() == "asc":
                direction = asc
            elif sort_order.lower() == "desc":
                direction = desc
            else:
                raise HTTPException(400, f"Invalid sort direction {sort_order}")
            order_by = direction(model.__table__.c[sort_column])

        return RequestParams(skip=skip, limit=limit, order_by=order_by)

    return inner


ItemRequestParams = Annotated[RequestParams, Depends(parse_react_admin_params(Item))]
