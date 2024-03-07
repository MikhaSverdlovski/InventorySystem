from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService


class DbActions:
    """Тут будет статика для действий с БД"""

    @staticmethod
    def add_item(name: str, descr: str, type_item: str, manufacturer: str, year: int, country: str, price: float,
                 quantity: int) -> bool:
        """Добавить элемент в таблицу с оружием"""
        try:
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """INSERT INTO item (name, description, type, manufacturer, year, country, price, quantity)
                            values (%s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(_SQL, (name, descr, type_item, manufacturer, year, country, price, quantity,))
                return True
        except Exception as e:
            print("Ошибка при обновлении элемента в базе данных:", e)
            return False

    @staticmethod
    def get_items() -> list:
        """Получить элементы из таблицы с оружием"""
        try:
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """SELECT * FROM item"""
                cursor.execute(_SQL)
                columns = [column[0] for column in cursor.description]  # Получаем имена столбцов
                items = []
                for row in cursor.fetchall():
                    item = dict(zip(columns, row))  # Создаем словарь из имен столбцов и значений строки
                    items.append(item)
            return items
        except Exception as e:
            print("Ошибка при получении элементов из базы данных:", e)
            return []

    @staticmethod
    def get_articles() -> list:
        """Получить все элементы из таблицы со статьями"""
        try:
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """SELECT * FROM articles"""
                cursor.execute(_SQL)
                columns = [column[0] for column in cursor.description]  # Получаем имена столбцов
                items = []
                for row in cursor.fetchall():
                    item = dict(zip(columns, row))  # Создаем словарь из имен столбцов и значений строки
                    items.append(item)
            return items
        except Exception as e:
            print("Ошибка при получении элементов из базы данных:", e)
            return []

    @staticmethod
    def get_item(item_id: int) -> dict:
        """Получить элемент из таблицы с оружием"""
        try:
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """SELECT * FROM item WHERE id = %s"""
                cursor.execute(_SQL, (item_id,))
                item = cursor.fetchone()
                if item:
                    columns = [column[0] for column in cursor.description]
                    item_dict = dict(zip(columns, item))
                    return item_dict
                else:
                    return {}  # Возвращаем пустой словарь, если элемент не найден
        except Exception as e:
            print("Ошибка при получении элемента из базы данных:", e)
            return {}

    @staticmethod
    def edit_item(item_id: int, name: str, descr: str, type_item: str, manufacturer: str, year: int, country: str,
                  price: float, quantity: int) -> bool:
        """Изменить элемент в таблице с оружием"""
        try:
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """UPDATE item SET name=%s, description=%s, type=%s, manufacturer=%s, year=%s, country=%s, price=%s, quantity=%s WHERE id=%s"""
                cursor.execute(_SQL, (name, descr, type_item, manufacturer, year, country, price, quantity, item_id))
            return True
        except Exception as e:
            print("Ошибка при обновлении элемента в базе данных:", e)
            return False
