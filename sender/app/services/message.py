from typing import Optional, NoReturn

import asyncio

from app import schemas
from app.config import bot_init


async def message_send(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    async with await bot_init() as bot:
        await bot.send_message(message.chat_id, message.text)


async def message_send_multiple(messages: list[schemas.PlainMessageSend]) -> Optional[NoReturn]:
    async with bot_init() as bot:
        await asyncio.gather(*[bot.send_message(msg.chat_id, msg.text) for msg in messages])
