from typing import Union
import os

# from .domain import test
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    passw = os.environ.get("DB_PASSWORD")

    return {"Hello": passw}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/root")
def root(q: int | None = None):
    return q
