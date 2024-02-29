import hashlib

from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

with SqlConnectorService(db_connect) as cursor:
    _SQL = """Select * from Items"""
    cursor.execute(_SQL)
    data = cursor.fetchall()





def check_password(password: str, user: str) -> bool:
    with SqlConnectorService(db_connect) as cursor:
        _SQL = """SELECT salt, passw_hash FROM users WHERE login = %s"""
        cursor.execute(_SQL, (user,))
        result = cursor.fetchone()
    hashed_password = hashlib.sha256((password + str(result[0])).encode()).hexdigest()
    return hashed_password == result[1]



print(check_password("asd","asd"))
