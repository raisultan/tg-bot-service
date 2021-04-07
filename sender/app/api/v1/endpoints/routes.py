from typing import Optional, NoReturn

from fastapi import APIRouter, status, UploadFile, File

from app import schemas
from app.services import message_send, message_send_multiple, tg_document_create

router = APIRouter()


@router.post('/send', status_code=status.HTTP_200_OK)
async def send_plain_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    # TODO: consider handling exception on unknown PEER_ID
    await message_send(chat_id=message.chat_id, text=message.text)
    return


@router.post('/send_multiple', status_code=status.HTTP_200_OK)
async def send_multiple_messages(messages: list[schemas.PlainMessageSend]) -> Optional[NoReturn]:
    # TODO: consider handling TG exceptions related to Timeout, TooMuchRequests, etc
    await message_send_multiple(messages)
    return


@router.post(
        '/create_document',
        response_model=schemas.DocumentCreate,
        status_code=status.HTTP_201_CREATED,
)
async def create_document(document: UploadFile = File(...))-> dict[str, str]:
    # TODO: consider handling TG exceptions related to Timeout, FileSize, etc
    doc_created = await tg_document_create(document)
    return doc_created
