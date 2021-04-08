from telethon import TelegramClient

from .settings import settings


async def bot_init() -> TelegramClient:
    bot = TelegramClient(
        session=settings.TG_SESSION_NAME,
        api_id=settings.TG_API_ID,
        api_hash=settings.TG_API_HASH,
    )

    return await bot.start(bot_token=settings.TG_BOT_TOKEN)
