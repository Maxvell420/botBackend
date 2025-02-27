from .connector import connector


class Base_repository:
    def __init__(self, conn: connector):
        self.connector: connector = conn

    def query(self, query: str, values: dict):
        self.connector.query(query, values)

    def next_row(self):
        return self.connector.next_row()
