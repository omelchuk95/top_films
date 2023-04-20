from pydantic import BaseModel


class FilmGenreBase(BaseModel):
    film_id: int | None = None
    genre_id: int | None = None


class FilmGenreCreate(BaseModel):
    id: int = None
    film_id: int
    genre_id: int


class FilmGenreInDBBase(FilmGenreBase):
    class Config:
        orm_mode = True


