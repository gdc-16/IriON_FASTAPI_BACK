from datetime import datetime

from pydantic import BaseModel, HttpUrl

from src.model import AnimalType


class AnimalBase(BaseModel):
    name: str | None
    animal_image_url: HttpUrl | None
    started_date: str | None
    content: str | None

    class Config:
        schema_extra: dict = {
            "example": {

            }
        }


class CreateAnimal(AnimalBase):
    name: str
    animal_image_url: HttpUrl
    type: AnimalType
    started_date: str
    shelter_id: int
    age: int
    content: str
    gender: str

    class Config:
        schema_extra: dict = {
            "example": {

            }
        }


class UpdaetAnimal(AnimalBase):
    pass
    