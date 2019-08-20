"""
Test module for the exam resource/endpoint.
"""
from starlette.testclient import TestClient
import pytest

from app.main import app
from app.exams.crud import create_exam
from app.database.base import db_session
from app.exams.schema import ExamCreate, Exam

client = TestClient(app)


@pytest.fixture()
def test_exam():
    test_exam_create = ExamCreate(name="new test", pass_value=50)
    test_exam_get = Exam(id=1, name="new test", pass_value=50)
    return test_exam_create, test_exam_get


def test_test_creation_success(db_fixture, token_fixture, test_exam):
    test_exam_create, test_exam_get = test_exam
    response = client.post("/exams/", json=test_exam_create.dict())

    assert response.status_code == 200
    assert response.json() == test_exam_get


def test_test_creation_fails_with_duplicate_entry(db_fixture, token_fixture, test_exam):
    test_exam_create, test_exam_get = test_exam
    create_exam(db_session, test_exam_create)

    response = client.post(f"/exams/", json=test_exam_create.dict())
    assert response.status_code == 400
    assert "exam with this name already exists" in response.json()["detail"]


def test_test_get(db_fixture, token_fixture, test_exam):
    test_exam_create, test_exam_get = test_exam
    exam = create_exam(db_session, test_exam_create)

    response = client.get(f"/exams/{exam.id}")
    assert response.status_code == 200
    assert response.json() == test_exam_get


def test_exam_creation_fails_without_authenticating(db_fixture, test_exam):
    test_exam_create, test_exam_get = test_exam
    response = client.post("/exams/", json=test_exam_create.dict())

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"


def test_exam_get_fails_without_authenticating(db_fixture, test_exam):
    test_exam_create, test_exam_get = test_exam
    exam = create_exam(db_session, test_exam_create)

    response = client.get(f"/exams/{exam.id}")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
