"""
This module defines the actual database ORM model of the Exam resource.
It is the representation that is used to describe how the database schema
will look.
"""
from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    pass_value = Column(Integer, nullable=False)
