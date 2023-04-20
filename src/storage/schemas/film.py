from pydantic import BaseModel


class FilmBase(BaseModel):
    name: str | None = None
    year: int | None = None


class FilmCreate(BaseModel):
    id: int = None
    name: str
    year: int


class FilmInDBBase(FilmBase):
    class Config:
        orm_mode = True


