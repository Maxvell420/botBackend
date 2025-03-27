from app.helpers import dd
from fastapi import Request
from . import Context


# Класс для авторизации


class AuthManager:

    def auth(self, req: Request, cntx: Context):
        headers = req.headers
        source = headers("source")
        match source:
            case "api":
                pasw = headers("pasw")
                login = headers("login")
                self._api_login(pasw=pasw, login=login)
            case None:
                exit(403)

    def _api_login(self, login: str | None, pasw: str | None):
        if login is None or pasw is None:
            exit(403)
