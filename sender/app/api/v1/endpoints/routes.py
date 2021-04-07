from typing import Optional, NoReturn
from fastapi import APIRouter, status

from app import schemas
from app.services import init_bot

router = APIRouter()


def send_specific(chat_id: str, text: str) -> Optional[NoReturn]:
    bot = init_bot()
    with bot:
        bot.send_message(
            chat_id=chat_id,
            text=text,
        )


@router.post("/send")
def send(
        data: schemas.SendSpecific,
        status_code=status.HTTP_200_OK,
) -> Optional[NoReturn]:

    send_specific(data.chat_id, data.text)
    return
