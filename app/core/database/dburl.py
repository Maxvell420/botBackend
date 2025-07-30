import os
from dotenv import load_dotenv

load_dotenv(".env", override=True)


user = os.getenv("PGSQL_USER")
host = os.getenv("DB_CONTANER_NAME")
database = os.getenv("DB_DATABASE")
passw = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
connection = os.getenv("DB_CONN")
driver = os.getenv("PG_DRIVER")


url = f"{connection}+{driver}://{user}:{passw}@db:{port}/{database}"
