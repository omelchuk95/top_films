from fastapi import APIRouter
from typing import Literal

from src.api.schemas.top_by_genre import GenreList
from src.storage.dto.film_genre_dto import film_genre_dto

router = APIRouter()


@router.get("/top/")
async def top(
        year: int,
        by: Literal["genres"] = "genres",
        row_count: int = 5
) -> GenreList:
    return film_genre_dto.get_top(year=year, limit=row_count)
