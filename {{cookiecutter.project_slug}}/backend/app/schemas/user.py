# from pydantic import BaseModel, EmailStr

from fastapi_users import models


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


# class CreateUserSchema(BaseModel):
# email: EmailStr
# password: str


# class UpdateUserSchema(BaseModel):
# email: EmailStr
# password: str


# class UserSchema(BaseModel):
# id: int
# email: EmailStr
# is_active: bool
# is_admin: bool
