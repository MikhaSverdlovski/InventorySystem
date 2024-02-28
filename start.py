from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

with SqlConnectorService(db_connect) as cursor:
    _SQL = """Select * from Items"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)
