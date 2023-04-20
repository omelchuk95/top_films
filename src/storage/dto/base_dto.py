from typing import Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.storage.database_main import secure_connection
from src.storage.models.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class DTOBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    @secure_connection
    def get(self, db: Session, *, o_id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == o_id).first()

    @secure_connection
    def get_all(self, db: Session) -> ModelType:
        return db.query(self.model).all()

    @secure_connection
    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
