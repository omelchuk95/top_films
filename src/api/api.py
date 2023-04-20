from fastapi import APIRouter

from src.api.endpoints import films

api_router = APIRouter()
api_router.include_router(films.router, prefix="/films", tags=["genres"])
