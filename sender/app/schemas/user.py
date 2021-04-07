from pydantic import BaseModel


class SendSpecific(BaseModel):
    chat_id: str
    text: str
