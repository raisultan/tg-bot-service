from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello() -> Dict[str, str]:
    return {'message': 'Hello World'}
