"""
This is the database access layer, all of the Create, Read Update Delete
functionality for users goes into this module.
"""
from sqlalchemy.orm import Session

from app.users import model, schema
from app.auth.hash import generate_password_hash


def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def create_user(db: Session, user: schema.UserCreate):
    hashed_password = generate_password_hash(user.password)
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
