from typing import Optional, NoReturn

from fastapi import APIRouter, status, UploadFile, File

from app import schemas
from app.services import (
    document_send,
    document_send_multiple,
    message_send,
    message_send_multiple,
    tg_document_create,
)

router = APIRouter()


@router.post('/send_message', status_code=status.HTTP_200_OK)
async def send_plain_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    # TODO: consider handling exception on unknown PEER_ID
    await message_send(message)
    return


@router.post('/send_multiple_messages', status_code=status.HTTP_200_OK)
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


@router.post('/send_document', status_code=status.HTTP_200_OK)
async def send_document(message: schemas.DocumentSend) -> Optional[NoReturn]:
    # TODO: handle potential exceptions
    await document_send(message)
    return


@router.post('/send_multiple_documents', status_code=status.HTTP_200_OK)
async def send_multiple_documents(messages: list[schemas.DocumentSend]) -> Optional[NoReturn]:
    # TODO: handle potential exceptions
    await document_send_multiple(messages)
    return
