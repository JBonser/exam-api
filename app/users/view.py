"""
This view module is solely responsible for handling the routing of
the application. It is the entrypoint of any web request for the user
resource.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.users import crud, schema
from app.depends import get_db

router = APIRouter()


@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schema.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)
