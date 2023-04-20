from sqlalchemy.orm import Session

from src.api.schemas.top_by_genre import GenreList
from src.storage.database_main import secure_connection
from src.storage.dto.base_dto import DTOBase
from src.storage.models.models import FilmGenreModel
from src.storage.schemas.film_genre import FilmGenreCreate
from sqlalchemy import text


class FilmGenreDTO(DTOBase[FilmGenreModel, FilmGenreCreate]):

    @secure_connection
    def get_top(self, db: Session, *, limit: int = 5, year: int):
        sql = "select al.genre_name, count(*) as total_films from " \
              '(select f.name as film_name, g."name" as genre_name from "film_genre" fg ' \
              'join "film" f ON f.Id = fg.film_id ' \
              f'join "genre" g ON g.Id = fg.genre_id where f.year={year}) al ' \
              f'group by al.genre_name order by total_films desc limit {limit}'
        result = db.execute(text(sql))
        return GenreList(genre_list=[{"name": i[0], "film_count": i[1]} for i in result.all()])

    @secure_connection
    def create(self, db: Session, *, film_id: int, genre_id: int):
        sql = f"INSERT INTO public.film_genre (film_id,genre_id) VALUES ({film_id},{genre_id});"
        db.execute(text(sql))
        db.commit()


film_genre_dto = FilmGenreDTO(FilmGenreModel)
