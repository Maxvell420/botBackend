import os
import copy
from .database import Connector

# Класс приходящий в контролеры в котором соединение и прочее


# Класс для загрузки подключений к базе данных (Если их будет несколько)
class Context:

    def __init__(self):
        self.connector = self.invoke_db_connector()

    def invoke_db_connector(self) -> Connector:
        host = os.environ.get("DB_HOST")
        port = os.environ.get("DB_PORT")
        user = os.environ.get("DB_USER")
        passw = os.environ.get("DB_PASSWORD")
        base = os.environ.get("DB_DATABASE")
        return Connector(user=user, password=passw, host=host, database=base, port=port)

    def get_connector(self) -> Connector:
        return copy.copy(self.connector)
