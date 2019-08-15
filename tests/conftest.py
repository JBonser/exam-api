"""
This module is automatically imported by pytest and so any fixtures
that need to be available to all/most tests should be defined here.
"""
import pytest

from app.database.base import init_database, destroy_database


@pytest.fixture()
def db_fixture(request):
    """
    Test fixture for performing the creation/destruction of the database, which is
    likely to be needed by almost all the tests.
    """
    init_database()
    request.addfinalizer(destroy_database)
