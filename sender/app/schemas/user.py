from typing import Optional

from pydantic import BaseModel


class PlainMessageSend(BaseModel):
    chat_id: int
    text: str


class DocumentCreate(BaseModel):
    document_id: str


class DocumentSend(BaseModel):
    chat_id: int
    caption: str
    document_id: str
