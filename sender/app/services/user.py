import io
from typing import Optional, NoReturn

import asyncio
from fastapi import UploadFile

from app import schemas
from app.config import settings
from .bot import init_bot


async def message_send(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    async with init_bot() as bot:
        await bot.send_message(
            chat_id=message.chat_id,
            text=message.text,
        )


async def message_send_multiple(messages: list[schemas.PlainMessageSend]) -> Optional[NoReturn]:
    async with init_bot() as bot:
        await asyncio.gather(*[bot.send_message(msg.chat_id, msg.text) for msg in messages])


async def tg_document_create(document: UploadFile) -> dict[str, str]:
    doc_bytes = io.BytesIO(document.file.read())
    doc_bytes.name = document.filename

    async with init_bot() as bot:
        msg = await bot.send_document(
                chat_id=settings.TG_FILES_CHAT_ID,
                document=doc_bytes,
        )

    # TODO: consider documenting potential exceptions
    doc_id = msg.document.file_id
    return {'document_id': doc_id}
