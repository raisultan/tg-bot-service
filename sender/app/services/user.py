from typing import Optional, NoReturn

from .services import init_bot


async def send_specific(chat_id: str, text: str) -> Optional[NoReturn]:
    async with init_bot() as bot:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
        )
