from fastapi import Request
from . import AuthManager, Context


class DepManger:
    def __init__(self, req: Request):
        self.req: Request = req
        self.cntx = Context()
        self.auth = AuthManager()
        self.auth.auth(req, self.cntx)
        req.state.dep: self = self
