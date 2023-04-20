from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str | None = None


class GenreCreate(GenreBase):
    id: int = None
    name: str


class GenreInDBBase(GenreBase):
    class Config:
        orm_mode = True


