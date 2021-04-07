from pydantic import BaseModel


class SendSpecific(BaseModel):
    chat_id: int
    text: str
