import pytest
from Service.SqlConnectorService import SqlConnectorService


# TODO:
#  - Разобраться с фикстурами, и привести в порядок


@pytest.fixture(scope="module")
def db_connection():
    connection = SqlConnectorService(
        host='127.0.0.1',
        user='dbadmin',
        password='Misha12345',
        database='Inventory'
    )
    connection.connect()
    yield connection
    connection.disconnect()


def test_connection(db_connection):
    assert db_connection.connection.is_connected(), "Connection should be established"
    assert db_connection.cursor is not None, "Cursor should be initialized"
