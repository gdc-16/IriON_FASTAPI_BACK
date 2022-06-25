from src.database import Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relation


class Shelter(Base):
    name: str = Column("name", String(length=32), nullable=False)
    location: str = Column("location", String(length=64), nullable=False)
    phone_number: str = Column(
        "phone_number", String(length=16), nullable=False
    )

    animal = relation("Animal", back_populates="animals")
