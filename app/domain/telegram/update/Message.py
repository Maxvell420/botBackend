from pydantic import BaseModel, Field
from .From import From
from app.domain.telegram.update.Chat import Chat


class Message(BaseModel):
    message_id: int
    from_: From = Field(..., alias="from")
    chat: Chat
