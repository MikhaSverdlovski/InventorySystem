import pytest
from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService
from security.Security import Security


class TestRegistration:
    @pytest.fixture(scope='class')
    def db_connection(self):
        # Подготавливаем фикстуру для подключения к базе данных
        connection_info = db_connect
        yield connection_info

    @pytest.fixture(scope='class', autouse=True)
    def cleanup_database(self, db_connection):
        # Очищаем базу данных перед выполнением каждого теста
        with SqlConnectorService(db_connect) as cursor:
            _SQL = """delete from users where email = 'qweqweqwe'"""
            cursor.execute(_SQL)

    @pytest.mark.parametrize("username, email, password",
                             [("qweqweqwe", "qweqweqwe", "qweqweqweqwe"),
                              ]
                             )
    def test_registration(self, username, email, password):
        assert Security.registration(username, email, password) == 'Success'
