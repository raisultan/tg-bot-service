from typing import Optional, NoReturn
from fastapi import APIRouter, status
from pyrogram import Client

from app import schemas
from app.services import init_bot

router = APIRouter()


async def send_specific(bot: Client, chat_id: str, text: str) -> Optional[NoReturn]:
    async with bot:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
        )


@router.post("/send")
async def send(
        data: schemas.SendSpecific,
        status_code=status.HTTP_200_OK,
) -> Optional[NoReturn]:

    bot = init_bot()
    bot.run(
        coroutine=await send_specific(
            bot=bot,
            chat_id=data.chat_id,
            text=data.text,
        ),
    )
    return
