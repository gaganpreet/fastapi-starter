from fastapi.params import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from app.deps.db import get_db
from app.deps.users import current_user
from app.models.item import Item as ItemModel
from app.schemas.item import Item, ItemCreate

router = SQLAlchemyCRUDRouter(
    schema=Item,
    create_schema=ItemCreate,
    db_model=ItemModel,
    db=get_db,
    dependencies=[Depends(current_user)],
)
