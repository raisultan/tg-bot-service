from typing import Optional, NoReturn
from fastapi import APIRouter, status

from app import schemas
from app.services import send_specific

router = APIRouter()


@router.post("/send")
async def send(
        data: schemas.SendSpecific,
        status_code=status.HTTP_200_OK,
) -> Optional[NoReturn]:

    await send_specific(data.chat_id, data.text)
    return
