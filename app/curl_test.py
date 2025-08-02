# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv(".env", override=True)

# bot_token = os.getenv("BOT_TOKEN")

# print(bot_token)

# response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
# print(response.text)

dict = {"name": "Alice", "name": "John"}

for key, value in dict.items():
    print(key)
    print(value)
