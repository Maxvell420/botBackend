import mysql.connector


class Connector:
    def __init__(self, user: str, password: str, host: str, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connectin = None
        self.cursor = None

    def connect(self) -> mysql.connector.MySQLConnection:
        return mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
        )

    def getConnect(self, func):
        if self.connection == None:
            self.connection = self.connect()
        return func

    @getConnect
    def query(self, query: str, values: dict | None):
        self.cursor = self.connect.cursor()
        self.cursor.execute(query, values)

    def FetchRow(self) -> tuple | None:
        if not (self.cursor == None):
            return self.row
        return None

    def nextRow(self) -> bool:
        if not (self.cursor == None):
            self.row = None
            return False

        self.row = self.cursor.fetchone()
        return True
