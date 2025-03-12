from typing import Union
from .domain import UserRepository
from .core import connector
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    user = os.environ.get("DB_USER")
    passw = os.environ.get("DB_PASSWORD")
    base = os.environ.get("DB_DATABASE")
    conn = connector(user=user, password=passw, host=host, database=base, port=port)
    repo = UserRepository(conn)
    data = repo.all()
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/root")
def root(q: int | None = None):
    return q
