from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService


class DbActions:
    """Тут будет статика для действий с БД"""

    @staticmethod
    def add_item(name: str, descr: str, type_item: str, manufacturer: str, year: int, country: str, price: float, quantity: int) -> bool:
        """Добавить элемент в таблицу"""
        with SqlConnectorService(db_connect) as cursor:
            _SQL = """INSERT INTO item (name, description, type, manufacturer, year, country, price, quantity)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (name, descr, type_item, manufacturer, year, country, price, quantity,))
        return True

    @staticmethod
    def get_items() -> list:
        """Получить элементы из таблицы"""
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
