from pydantic import BaseModel
from typing import List, Union, Optional
from app.domain.telegram.update.MyChatMember import MyChatMember
from app.domain.telegram.update.Message import Message


class Response(BaseModel):
    update_id: int
    my_chat_member: Optional[MyChatMember] = None
    message: Optional[Message] = None
