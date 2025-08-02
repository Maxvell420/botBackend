from .core import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from .domain import User, Update, MyChatMember, Message
from fastapi import FastAPI, Body

from .core import url

app = FastAPI()


@app.get("/")
def read(db: Session = Depends(get_db)):
    # user = db.query(User).filter(User.id == user_id).first()
    # return url
    return {1: 1}


@app.post("/delete_webhook")
def delete_webhook(data: Update, db: Session = Depends(get_db)):
    messages = data.result

    for message in messages:
        if message.my_chat_member:
            user = User(username=message.my_chat_member.from_.username)
            db.add(user)
            db.commit()

    return
