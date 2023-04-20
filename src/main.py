from fastapi import FastAPI

from src.api.api import api_router
from src.storage.dto.genre_dto import genre_dto
from src.utils.initial_data import get_initial_data

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    if not genre_dto.get_all():
        get_initial_data()
