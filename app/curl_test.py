import requests
import os
from dotenv import load_dotenv
import time

load_dotenv(".env", override=True)
webhook_url = os.getenv("WEBHOOK_URL")
bot_token = os.getenv("BOT_TOKEN")

while True:
    time.sleep(3)
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
    requests.post(f"http://localhost:8000/recycleUpdates", data=response.text)

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
    time.sleep(1)
    requests.get(
        f"https://api.telegram.org/bot{bot_token}/deleteWebhook",
    )
