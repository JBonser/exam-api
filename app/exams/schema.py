"""
The schema module is responsible for defining the serialization models
for the exam resource. It is used to provide validation of the data payloads
of the routes in the view module.
"""
from pydantic import BaseModel


class ExamCreate(BaseModel):
    name: str
    pass_value: int


class Exam(ExamCreate):
    id: int

    class Config:
        orm_mode = True
