from pydantic import BaseModel
from typing import List
from .Response import Response


class Update(BaseModel):
    ok: bool
    result: List[Response]
