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
    user = os.environ.get("DB_USERNAME")
    passw = os.environ.get("DB_PASSWORD")
    base = os.environ.get("DB_DATABASE")
    conn = connector(user, passw, host, base, port)
    repo = UserRepository(conn)
    return {"Hello": passw}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/root")
def root(q: int | None = None):
    return q
