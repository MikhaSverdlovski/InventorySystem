from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

with SqlConnectorService(db_connect) as cursor:
    _SQL = """Select * from Items"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)

with SqlConnectorService(db_connect) as cursor:
    _SQL = """INSERT INTO users (login, passw_hash, salt) VALUES (%s, %s, %s)"""
    cursor.execute(_SQL, ('Mikhail', 234234, 54,))
