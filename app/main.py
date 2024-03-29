"""
This is the main entrypoint to the application, the app variable that is
defined here is what is used by the web server to create the application
workers.
"""
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from app.users.view import router as user_router
from app.auth.view import router as auth_router
from app.exams.view import router as exam_router
from app.database.base import Session

app = FastAPI(title="Exam API")
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(exam_router, prefix="/exams", tags=["exams"])


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = Session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
