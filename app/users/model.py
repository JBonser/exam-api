"""
This module defines the actual database ORM model of the User resource.
It is the representation that is used to describe how the database schema
will look.
"""
from sqlalchemy import Boolean, Column, Integer, String

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
