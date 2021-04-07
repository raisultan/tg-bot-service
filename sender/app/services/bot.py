from typing import NoReturn, Optional
from pyrogram import Client

from app.config import settings


def init_bot() -> Client:
    bot = Client(
        session_name=settings.TG_SESSION_NAME,
        api_id=settings.TG_API_ID,
        api_hash=settings.TG_API_HASH,
        bot_token=settings.TG_BOT_TOKEN,
    )

    return bot
