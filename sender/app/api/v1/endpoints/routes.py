from fastapi import APIRouter
from pyrogram import Client

from app.config import settings

router = APIRouter()

# bot client declaration example
bot = Client(
    session_name='sample_session',
    bot_token=settings.TG_BOT_TOKEN,
)


@router.get("/")
async def hello() -> dict[str, str]:
    return {'message': 'Hello World'}
