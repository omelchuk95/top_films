from functools import wraps
from typing import Callable, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings


engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def secure_connection(fn: Callable) -> Any:
    @wraps(fn)
    def decorated(*args: Any, **kwargs: Any) -> Any:
        try:
            db = kwargs["db"] = kwargs.get("db", _SessionLocal())
            result = fn(*args, **kwargs)
            return result
        finally:
            db.close()

    return decorated
