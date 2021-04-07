import io
from typing import Optional, NoReturn
from fastapi import UploadFile

from app.config import settings
from .bot import init_bot


async def message_send(chat_id: str, text: str) -> Optional[NoReturn]:
    async with init_bot() as bot:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
        )


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
