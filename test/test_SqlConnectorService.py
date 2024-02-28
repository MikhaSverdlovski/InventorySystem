import pytest
from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

@pytest.fixture(scope='module')
def db_connection():
    # Подготавливаем фикстуру для подключения к базе данных
    connection_info = db_connect
    yield connection_info

@pytest.fixture(scope='module')
def sql_service(db_connection):
    # Подготавливаем фикстуру для сервиса работы с базой данных
    with SqlConnectorService(db_connect) as cursor:
        yield cursor


def test_sql_service_enter(db_connection):
    # Проверяем, что __enter__ метод устанавливает соединение с базой данных
    with SqlConnectorService(db_connect) as cursor:
        # Проверяем, что курсор не равен None
        assert cursor is not None


