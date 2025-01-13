from typing import Union
from .domain import test
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@test.prov
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
