import hashlib

from Service.DbActions import DbActions
from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""


def get_item(item_id: int) -> list:
    """Получить все элементы из таблицы со статьями"""
    try:
        with SqlConnectorService(db_connect) as cursor:
            _SQL = """SELECT * FROM item where id = %s"""
            cursor.execute(_SQL, (item_id,))
            item = cursor.fetchone()
            return item
    except Exception as e:
        print("Ошибка при получении элементов из базы данных:", e)
        return []

print(get_item(21))
