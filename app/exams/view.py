"""
This view module is solely responsible for handling the routing of
the application. It is the entrypoint of any web request for the exam
resource.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.exception import DuplicateResourceError
from app.exams import crud, schema
from app.users.schema import User
from app.depends import get_db
from app.auth.depends import login_required

router = APIRouter()


@router.post("/", response_model=schema.Exam)
async def create_exam(
    exam: schema.ExamCreate,
    db: Session = Depends(get_db),
    user: User = Depends(login_required),
):
    if crud.get_exam_by_name(db, exam.name):
        raise DuplicateResourceError(resource="exam", value="name")
    return crud.create_exam(db=db, exam=exam)


@router.get("/{exam_id}", response_model=schema.Exam)
async def get_exam(
    exam_id: int, db: Session = Depends(get_db), user: User = Depends(login_required)
):
    return crud.get_exam(db, exam_id)
