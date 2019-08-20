"""
This is the database access layer, all of the Create, Read Update Delete
functionality for exams go into this module.
"""
from sqlalchemy.orm import Session

from app.exams import model, schema


def get_exam(db: Session, exam_id: int):
    return db.query(model.Exam).filter(model.Exam.id == exam_id).first()


def get_exam_by_name(db: Session, name: str):
    return db.query(model.Exam).filter(model.Exam.name == name).first()


def create_exam(db: Session, exam: schema.ExamCreate):
    exam = model.Exam(name=exam.name, pass_value=exam.pass_value)
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam
