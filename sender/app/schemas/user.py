from pydantic import BaseModel


class PlainMessageSend(BaseModel):
    chat_id: int
    text: str


class DocumentCreate(BaseModel):
    document_id: str
