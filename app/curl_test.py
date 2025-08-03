import requests
import os
from dotenv import load_dotenv

load_dotenv(".env", override=True)

bot_token = os.getenv("BOT_TOKEN")

# print(bot_token)

response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
# requests.get(
#     f"https://api.telegram.org/bot{bot_token}/sendMessage",
#     params={"chat_id": 1955425357, "text": f"hello"},
# )
# response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
print(response.text)
