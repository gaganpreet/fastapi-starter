from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException
from sqlalchemy import func, select
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import ItemRequestParams
from app.deps.users import CurrentUser
from app.models.item import Item
from app.schemas.item import Item as ItemSchema
from app.schemas.item import ItemCreate, ItemUpdate

router = APIRouter(prefix="/items")


@router.get("", response_model=List[ItemSchema])
async def get_items(
    response: Response,
    session: CurrentAsyncSession,
    request_params: ItemRequestParams,
    user: CurrentUser,
) -> Any:
    total = await session.scalar(
        select(func.count(Item.id).filter(Item.user_id == user.id))
    )
    items = (
        (
            await session.execute(
                select(Item)
                .offset(request_params.skip)
                .limit(request_params.limit)
                .order_by(request_params.order_by)
                .filter(Item.user_id == user.id)
            )
        )
        .scalars()
        .all()
    )
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(items)}/{total}"
    return items


@router.post("", response_model=ItemSchema, status_code=201)
async def create_item(
    item_in: ItemCreate,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    item = Item(**item_in.dict())
    item.user_id = user.id
    session.add(item)
    await session.commit()
    return item


@router.put("/{item_id}", response_model=ItemSchema)
async def update_item(
    item_id: int,
    item_in: ItemUpdate,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    item: Optional[Item] = await session.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404)
    update_data = item_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
    session.add(item)
    await session.commit()
    return item


@router.get("/{item_id}", response_model=ItemSchema)
async def get_item(
    item_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    item: Optional[Item] = await session.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404)
    return item


@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    item: Optional[Item] = await session.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(404)
    await session.delete(item)
    await session.commit()
    return {"success": True}
