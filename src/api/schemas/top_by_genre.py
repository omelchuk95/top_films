from pydantic import BaseModel


class Genre(BaseModel):
    name: str
    film_count: int


class GenreList(BaseModel):
    genre_list: list[Genre]
