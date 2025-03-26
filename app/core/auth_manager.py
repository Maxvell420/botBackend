from fastapi import Request
from . import Context

# Класс для авторизации


class AuthManager:

    def auth(self, req: Request, cntx: Context):
        headers = dict(req.headers)
        with open("log.txt", encoding="utf-8") as file:
            for key in headers:
                # file.write(key)
