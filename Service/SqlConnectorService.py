import mysql.connector

class SqlConnectorService:
    #TODO: Переписать нормально с менеджером контекста

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def connect_with(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
            return self.connection, self.cursor
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return None, None

    def disconnect_with(self, connection, cursor):
        if connection:
            cursor.close()
            connection.close()
            print("Disconnected from the database")

    def __enter__(self):
        self.connect_with()
        return self.connection, self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect_with(self.connection, self.cursor)
