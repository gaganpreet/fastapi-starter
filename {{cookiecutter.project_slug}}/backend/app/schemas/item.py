from pydantic import BaseModel


class ItemCreate(BaseModel):
    value: str


class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
