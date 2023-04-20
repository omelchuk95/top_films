from sqlalchemy import Integer, Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from src.storage.models.base_model import Base


FilmGenreModel = Table(
    "film_genre",
    Base.metadata,
    Column("film_id", Integer, ForeignKey("film.id")),
    Column("genre_id", Integer, ForeignKey("genre.id")),
)


class FilmModel(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)


class GenreModel(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

