from typing import Optional, NoReturn
from fastapi import APIRouter, status, UploadFile, File

from app import schemas
from app.services import message_send, tg_document_create

router = APIRouter()


@router.post('/send', status_code=status.HTTP_200_OK)
async def send_plain_message(data: schemas.PlainMessageSend) -> Optional[NoReturn]:
    await message_send(chat_id=data.chat_id, text=data.text)
    return


@router.post(
        '/create_document',
        response_model=schemas.DocumentCreate,
        status_code=status.HTTP_201_CREATED,
)
async def create_document(document: UploadFile = File(...))-> dict[str, str]:
    data = await tg_document_create(document)
    return data
