from functools import lru_cache

from src.config.settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
