from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LEVEL: str
    PROJECT_TITLE: str = "이리ON"
    PROJECT_VERSION: int = 1
    PROJECT_DESCRIPTION: str = "GDG Campus Korea 2022 오프티벌 팀 돌봐조 이리ON API"

    class Config:
        env_file = ".env"


class DevelopSettings(Settings):
    DB_URL: str = Field(env="DEVELOP_DB_URL")
    ALLOW_ORIGINS: list[str] = [
        "http://localhost:3000",
        "https://d15s9x1ybtvbwb.cloudfront.net",
    ]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ['*']
    ALLOW_HEADERS: list[str] = ['*']


class ProductSettings(Settings):
    DB_URL: str = Field(env="PRODUCT_DB_URL")
    ALLOW_ORIGINS: list[str] = [
        "http://localhost:3000",
        "https://d15s9x1ybtvbwb.cloudfront.net",
    ]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ['*']
    ALLOW_HEADERS: list[str] = ['*']


@lru_cache
def get_settings():
    if Settings().LEVEL == "DEVELOP":
        return DevelopSettings()

    else:
        return ProductSettings()
