from .core import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from .domain import User
from fastapi import FastAPI, Request

from .core import url

app = FastAPI()


@app.get("/")
def read(db: Session = Depends(get_db)):
    # user = db.query(User).filter(User.id == user_id).first()
    # return url
    return {1: 1}
