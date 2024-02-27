from Service.SqlConnectorService import SqlConnectorService

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

connection_service = SqlConnectorService('127.0.0.1', 'dbadmin', 'Misha12345', 'Inventory')

with connection_service as (connection, cursor):
    if connection is not None:
        # Выполнение запросов с использованием курсора
        cursor.execute("SELECT * FROM Items")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
