# from pydantic import BaseModel, EmailStr

from fastapi_users import models


class User(models.BaseUser):
    pass

    class Config:
        orm_mode = True


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
