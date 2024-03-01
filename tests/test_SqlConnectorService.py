import pytest
from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

class TestSqlService:
    @pytest.fixture(scope='module')
    def db_connection(self):
        # Подготавливаем фикстуру для подключения к базе данных
        connection_info = db_connect
        yield connection_info

    @pytest.fixture(scope='function')
    def sql_service(self, db_connection):
        # Подготавливаем фикстуру для сервиса работы с базой данных
        with SqlConnectorService(db_connect) as cursor:
            yield cursor

    def test_sql_service_enter(self, db_connection):
        # Проверяем, что __enter__ метод устанавливает соединение с базой данных
        with SqlConnectorService(db_connect) as cursor:
            # Проверяем, что курсор не равен None
            assert cursor is not None
