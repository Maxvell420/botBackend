from .connector import Connector


class BaseRepository:

    def __init__(self, conn: Connector):
        self.table = "default_table"
        self.connector: Connector = conn

    def query(self, query: str, values: dict = None):
        self.connector.query(query, values)

    def next_row(self):
        return self.connector.next_row()

    def all(self):
        self.connector.query("SELECT * FROM " + self.table)
        data = []

        while self.connector.next_row():
            data.append(self.connector.fetch_row())
        return data

    # def findByWhere(self,where:str):
