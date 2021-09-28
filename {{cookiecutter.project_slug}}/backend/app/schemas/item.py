from pydantic.main import BaseModel
from pydantic.types import UUID4


class ItemCreate(BaseModel):
    value: str


class Item(ItemCreate):
    id: UUID4

    class Config:
        orm_mode = True
