import enum
from datetime import datetime

from pydantic import HttpUrl
from sqlalchemy import Column, String, Enum, ForeignKey, DateTime

from src.database import Base


class AnimalType(str, enum.Enum):
    DOG = "dog"
    CAT = "cat"


class Animal(Base):
    name: str = Column("name", String(length=8), nullable=False)
    animal_image_url: HttpUrl = Column(
        "animal_image_url", String(512), nullable=False
    )
    type: AnimalType = Column("type", Enum(AnimalType), nullable=False)
    started_date: datetime = Column("started_date", DateTime(), nullable=False)
    shelter_id: int = Column(
        "shelter_id", ForeignKey("shelters.id", ondelete="CASCADE")
    )
