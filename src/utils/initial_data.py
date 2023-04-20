import csv

from src.storage.dto.genre_dto import genre_dto
from src.storage.dto.film_dto import film_dto
from src.storage.dto.film_genre_dto import film_genre_dto
from src.storage.schemas.genre import GenreCreate
from src.storage.schemas.film import FilmCreate

cache = {}


def create_genre(genre: str) -> int:
    if genre not in cache.keys():
        genre_id = genre_dto.create(obj_in=GenreCreate(name=genre)).id
        cache[genre] = genre_id
    return cache[genre]


def get_initial_data():
    print("Test data is being loaded...")

    with open("movies.tsv") as f:
        rd = csv.reader(f, delimiter="\t", quotechar='"')
        for row in rd:
            name = row[2]
            genres = row[-1]
            year = row[-3]
            if genres in (r"\N", "genres"):
                continue

            film_id = film_dto.create(obj_in=FilmCreate(name=name, year=year)).id
            for genre in genres.split(","):
                genre_id = create_genre(genre)

                film_genre_dto.create(film_id=film_id, genre_id=genre_id)

