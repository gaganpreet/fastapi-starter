from fastapi.params import Depends

from app.api.crud._crudrouter import ReactAdminCompatibleCRUDRouter
from app.deps.db import get_db
from app.deps.users import current_user
from app.models.item import Item as ItemModel
from app.schemas.item import Item, ItemCreate

router = ReactAdminCompatibleCRUDRouter(
    schema=Item,
    create_schema=ItemCreate,
    db_model=ItemModel,
    db=get_db,
    dependencies=[Depends(current_user)],
)
