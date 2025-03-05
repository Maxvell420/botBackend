import mysql.connector


class connector:
    def __init__(self, user: str, password: str, host: str, database: str, port: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None
        self.row = None

    def connect(self) -> mysql.connector.MySQLConnection:
        return mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
            port=self.port,
        )

    def getConnect(self):
        if self.connection is None:
            self.connection = self.connect()

    def query(self, query: str, values: dict | None):
        self.getConnect()
        self.cursor = self.connect().cursor()
        self.cursor.execute(query, values)

    def fetch_row(self) -> tuple | None:
        if not self.cursor is None:
            return self.row
        return None

    def next_row(self) -> bool:
        if not self.cursor is None:
            self.row = None
            return False

        self.row = self.cursor.fetchone()
        return True
