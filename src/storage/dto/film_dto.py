from src.storage.dto.base_dto import DTOBase
from src.storage.models.models import FilmModel
from src.storage.schemas.film import FilmCreate


class FilmDTO(DTOBase[FilmModel, FilmCreate]):
    pass


film_dto = FilmDTO(FilmModel)
