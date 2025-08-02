from pydantic import BaseModel
from typing import List


class Chat(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
