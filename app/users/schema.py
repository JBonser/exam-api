"""
The schema module is responsible for defining the serialization models
for the user resource. It is used to provide validation of the data payloads
of the routes in the view module.
"""
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    surname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
