"""
This module is automatically imported by pytest and so any fixtures
that need to be available to all/most tests should be defined here.
"""
import pytest

from app.main import app
from app.database.base import init_database, destroy_database
from app.auth.depends import login_required
from tests.dependency_overrides import login_required_override


@pytest.fixture()
def db_fixture(request):
    """
    Test fixture for performing the creation/destruction of the database, which is
    likely to be needed by almost all the tests.
    """
    init_database()
    request.addfinalizer(destroy_database)


@pytest.fixture()
def token_fixture(request):
    """
    Test fixture for overriding the login_required token dependency
    This allows us to more easily test the logic of the routes, without
    being tripped up by the authentication constantly.
    """
    app.dependency_overrides[login_required] = login_required_override

    def teardown():
        app.dependency_overrides = {}

    request.addfinalizer(teardown)
