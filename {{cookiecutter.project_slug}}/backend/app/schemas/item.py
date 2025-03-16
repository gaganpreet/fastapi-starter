from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    value: str


class ItemUpdate(ItemCreate):
    pass


class Item(ItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
