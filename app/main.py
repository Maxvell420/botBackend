from typing import Union
from .domain.User import user_repository
from fastapi import FastAPI, Depends
from .core import dep_manager

app = FastAPI()


@app.get("/")
def read_root(req=Depends(dep_manager)):
    return req
    repo = user_repository(req.connector)
    data = repo.all()
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/root")
def root(q: int | None = None):
    return q
