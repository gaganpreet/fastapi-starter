import json
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import asc, desc
from starlette.responses import Response

from app.deps.db import get_db
from app.deps.request_params import parse_react_admin_params
from app.deps.users import current_user
from app.models.item import Item
from app.models.user import User
from app.schemas.item import Item as ItemSchema
from app.schemas.item import ItemCreate
from app.schemas.request_params import RequestParams

router = APIRouter(prefix="/items")


def parse_request(model, sort_, range_):
    skip, limit = 0, 10
    if range_:
        start, end = json.loads(range_)
        skip, limit = start, (end - start + 1)

    order_by = desc(model.id)
    if sort_:
        sort_column, sort_order = json.loads(sort_)
        if sort_order.lower() == "asc":
            direction = asc
        elif sort_order.lower() == "desc":
            direction = desc
        else:
            raise HTTPException(400, f"Invalid sort direction {sort_order}")
        order_by = direction(model.__table__.c[sort_column])

    return skip, limit, order_by


@router.get("/", response_model=List[ItemSchema])
def get_items(
    response: Response,
    db: Session = Depends(get_db),
    request_params: RequestParams = Depends(parse_react_admin_params(Item)),
    user: User = Depends(current_user),
) -> Any:
    total = db.scalar(select(func.count(Item.id).filter(Item.user_id == user.id)))
    items = (
        db.execute(
            select(Item)
            .offset(request_params.skip)
            .limit(request_params.limit)
            .order_by(request_params.order_by)
            .filter(Item.user_id == user.id)
        )
        .scalars()
        .all()
    )
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(items)}/{total}"
    return items


@router.post("/", response_model=ItemSchema)
def create_item(
    item_in: ItemCreate,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
) -> Any:
    item = Item(**item_in.dict())
    item.user_id = user.id
    db.add(item)
    db.commit()
    return item


@router.get("/{item_id}/", response_model=ItemSchema)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
) -> Any:
    item: Optional[Item] = db.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404)
    return item


@router.delete("/{item_id}/")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(current_user),
) -> Any:
    item: Optional[Item] = db.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404)
    db.delete(item)
    db.commit()
    return {"success": True}
