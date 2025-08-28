from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent.parent / ".env"),
        extra="ignore",
    )

    app_name: str = "Pantry API"
    environment: str = "dev"
    database_url: str = "sqlite:///./pantry.db"  # default local dev
    testing: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
