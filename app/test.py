import requests
from .core import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from .domain import User, Update, MyChatMember, Message
from fastapi import FastAPI, Body
from .core import url
import os
from dotenv import load_dotenv

bot_token = os.getenv("BOT_TOKEN")
app = FastAPI()


@app.get("/")
def read(db: Session = Depends(get_db)):
    # user = db.query(User).filter(User.id == user_id).first()
    # return url
    return {1: 1}


@app.post("/delete_webhook")
def delete_webhook():
    requests.get(
        f"https://api.telegram.org/bot{bot_token}/deleteWebhook",
    )
    return


@app.post("/recycleUpdates")
def recycleUpdates(data: Update, db: Session = Depends(get_db)):
    messages = data.result

    user = User(json=data.model_dump_json())
    db.add(user)
    db.commit()

    for message in messages:
        if message.message:
            username = message.message.from_.username
            chat_id = message.message.chat.id
            requests.get(
                f"https://api.telegram.org/bot{bot_token}/sendMessage",
                params={"chat_id": chat_id, "text": f"hello {username}"},
            )
    return


@app.post("/setUpWebhook")
def set_up_webhook():
    load_dotenv(".env", override=True)
    webhook_url = os.getenv("WEBHOOK_URL")
    requests.get(
        f"https://api.telegram.org/bot{bot_token}/setWebhook",
        params={
            "url": webhook_url,
            # Дополнительные параметры (опционально):
            "max_connections": 1,  # макс. количество соединений (1-100)
            "allowed_updates": ["message", "callback_query"],  # типы обновлений
            "drop_pending_updates": True,  # удалить pending updates
        },
    )
    return
