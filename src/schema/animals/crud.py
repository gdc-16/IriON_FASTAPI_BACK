from datetime import datetime

from pydantic import HttpUrl

from src.model import AnimalType
from src.schema.crud_base import CRUDSchemaBase


class AnimalBase(CRUDSchemaBase):
    name: str | None
    animal_image_url: HttpUrl | None
    started_date: datetime | None

    class Config:
        schema_extra: dict = {
            "example": {

            }
        }


class CreateAnimal(AnimalBase):
    name: str
    animal_image_url: HttpUrl
    type: AnimalType
    started_date: datetime
    shelter_id: int

    class Config:
        schema_extra: dict = {
            "example": {

            }
        }


class UpdaetAnimal(AnimalBase):
    pass
    