import hashlib

from Service.DbActions import DbActions
from Service.SqlConnectorService import SqlConnectorService
from Config import db_connect

#TODO: Потом вообще убрать это
"""Тестовый файл для теста коннекта к БД"""

print(DbActions.get_items())
