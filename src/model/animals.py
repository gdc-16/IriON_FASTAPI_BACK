import enum
from datetime import datetime

from pydantic import HttpUrl
from sqlalchemy import Column, String, Enum, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relation

from src.database import Base


class AnimalType(str, enum.Enum):
    DOG = "dog"
    CAT = "cat"


class Animal(Base):
    id: int = Column("id", Integer, primary_key=True, autoincrement=True)
    name: str = Column("name", String(length=8), nullable=False)
    animal_image_url: HttpUrl = Column(
        "animal_image_url", String(512), nullable=False
    )
    type: AnimalType = Column("type", Enum(AnimalType), nullable=False)
    started_date: datetime = Column("started_date", DateTime(), nullable=False)
    shelter_id: int = Column(
        "shelter_id", ForeignKey("shelters.id", ondelete="CASCADE")
    )
    age: int = Column("age", Integer, nullable=False)
    content: str = Column("content", String(length=32), nullable=False)
    gender: str = Column("gender", String(length=1), nullable=False)

    users = relation("User", secondary="follows", back_populates="animals")
    shelters = relation("Shelter", back_populates="animals")
