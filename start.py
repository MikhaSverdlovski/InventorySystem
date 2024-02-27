from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

connection_service = SqlConnectorService(**db_connect)

with connection_service as (connection, cursor):
    if connection is not None:
        # Выполнение запросов с использованием курсора
        cursor.execute("SELECT * FROM Items")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
