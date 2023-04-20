from src.storage.dto.base_dto import DTOBase
from src.storage.models.models import GenreModel
from src.storage.schemas.genre import GenreCreate


class GenreDTO(DTOBase[GenreModel, GenreCreate]):
    pass


genre_dto = GenreDTO(GenreModel)
