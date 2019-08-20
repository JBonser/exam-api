"""
This view module is solely responsible for handling the routing of
the application. It is the entrypoint of any web request for the user
resource.
"""
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session

from app.users import crud, schema
from app.users.model import User
from app.depends import get_db
from app.auth.depends import login_required

router = APIRouter()


@router.post("/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="A user with this e-mail already exists",
        )
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schema.User)
async def get_user(
    user_id: int, db: Session = Depends(get_db), user: User = Depends(login_required)
):
    return crud.get_user(db, user_id)
