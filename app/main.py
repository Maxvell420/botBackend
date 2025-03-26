from typing import Union
from fastapi import FastAPI, Request, Depends
from .core import DepManger


# from .domain.User import UserRepository

app = FastAPI(dependencies=[Depends(DepManger)])


@app.get("/")
def read_root(req: Request):
    return req.state.dep.auth.str
    # repo = UserRepository()
    return ""


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/root")
def root(q: int | None = None):
    return q
