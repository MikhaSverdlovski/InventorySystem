from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService
from security import Security


def test_registration_success(username = 'qweqweqwwe', email = 'qweqweqwe', password = 'qweqweqweqwe'):
    with SqlConnectorService(db_connect) as cursor:
        _SQL = """delete from users where login = %s"""
        cursor.execute(_SQL, (username,))
    assert Security.registration(username,email,password) == 'Success'


def test_registration_failed(username = 'asd', email = 'qweqweqwe', password = 'qweqweqweqwe'):
    result = Security.registration(username,email,password)
    assert result.startswith("Error:")