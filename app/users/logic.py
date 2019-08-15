"""
This module is here to provide business level logic.
The view, schema, crud and model modules have specific jobs which
should not get littered with business logic. It is this module that should
be used to place any of this additional behaviour.
"""
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return crypt_context.verify(plain_password, hashed_password)


def generate_password_hash(password: str):
    return crypt_context.hash(password)
