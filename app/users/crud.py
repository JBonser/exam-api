"""
This is the database access layer, all of the Create, Read Update Delete
functionality for users goes into this module.
"""
from sqlalchemy.orm import Session

from . import model, schema, logic


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    hashed_password = logic.generate_password_hash(user.password)
    user = model.User(
        first_name=user.first_name,
        surname=user.surname,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
