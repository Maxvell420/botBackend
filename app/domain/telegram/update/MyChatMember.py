from pydantic import BaseModel, Field
from .From import From
from .Chat import Chat


class MyChatMember(BaseModel):
    chat: Chat
    from_: From = Field(..., alias="from")
