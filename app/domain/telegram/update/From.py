from pydantic import BaseModel
from typing import List


class From(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
