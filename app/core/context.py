# Класс приходящий в контролеры в котором соединение и прочее
import os
from .database import Connector


class Context:

    def __init__(self):
        self.connector = self.get_db_connector()

    def get_db_connector(self) -> Connector:
        host = os.environ.get("DB_HOST")
        port = os.environ.get("DB_PORT")
        user = os.environ.get("DB_USER")
        passw = os.environ.get("DB_PASSWORD")
        base = os.environ.get("DB_DATABASE")
        return Connector(user=user, password=passw, host=host, database=base, port=port)
