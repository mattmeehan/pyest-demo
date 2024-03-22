import pytest

from pytest_demo.database import Database


@pytest.fixture
def db():
    users = [
        {"id": "123", "name": "Joe"},
        {"id": "456", "name": "Donald"},
        {"id": "789", "name": "Hillary"},
    ]
    database = Database(users)
    database.connect()
    yield database  # Provide the setup database to the test
    database.disconnect()


def test_database_get_users(db):
    assert db.get_users() == [
        {"id": "123", "name": "Joe"},
        {"id": "456", "name": "Donald"},
        {"id": "789", "name": "Hillary"},
    ]
