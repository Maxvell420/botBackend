from .connector import connector


class Base_repository:
    def __init__(self, conn: connector, table: str = "default_table"):
        self.table: str = table
        self.connector: connector = conn

    def query(self, query: str, values: dict = None):
        self.connector.query(query, values)

    def next_row(self):
        return self.connector.next_row()

    def all(self):
        return self.connector.query("SELECT * FROM " + self.table)
        # data = {}
        # while self.connector.next_row():
        #     data.update(self.connector.fetch_row())
        # return data
