import io
from typing import Optional, NoReturn

from fastapi import UploadFile

from app import schemas
from app.config import settings
from .bot import init_bot


def message_send(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    with init_bot() as bot:
        bot.send_message(
            chat_id=message.chat_id,
            text=message.text,
        )


def message_send_multiple(messages: list[schemas.PlainMessageSend]) -> Optional[NoReturn]:
    with init_bot() as bot:
        for msg in messages:
            bot.send_message(msg.chat_id, msg.text)


def tg_document_create(document: UploadFile) -> dict[str, str]:
    doc_bytes = io.BytesIO(document.file.read())
    doc_bytes.name = document.filename

    with init_bot() as bot:
        msg = bot.send_document(
                chat_id=settings.TG_FILES_CHAT_ID,
                document=doc_bytes,
        )

    # TODO: consider handling potential exceptions
    doc_id = msg.document.file_id
    return {'document_id': doc_id}


def document_send(message: schemas.DocumentSend) -> Optional[NoReturn]:
    with init_bot() as bot:
        bot.send_document(
                chat_id=message.chat_id,
                caption=message.caption,
                document=message.document_id,
        )


def document_send_multiple(messages: list[schemas.DocumentSend]) -> Optional[NoReturn]:
    with init_bot() as bot:
        for msg in messages:
            bot.send_document(
                chat_id=msg.chat_id,
                caption=msg.caption,
                document=msg.document_id,
            )
