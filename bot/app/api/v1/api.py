from fastapi import APIRouter

from app.api.v1.endpoints.routes import router

api_router = APIRouter()
api_router.include_router(router, tags=['hello'])
