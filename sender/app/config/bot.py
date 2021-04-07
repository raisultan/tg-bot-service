from pyrogram import Client

from .settings import settings


def bot_init() -> Client:
    bot = Client(
        session_name=settings.TG_SESSION_NAME,
        api_id=settings.TG_API_ID,
        api_hash=settings.TG_API_HASH,
        bot_token=settings.TG_BOT_TOKEN,
    )
    return bot
