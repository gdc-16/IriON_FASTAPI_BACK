from email.policy import default
from src.database import Base

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relation


class Shelter(Base):
    id: int = Column("id", Integer, primary_key=True, autoincrement=True,)
    name: str = Column("name", String(length=32), nullable=False)
    location: str = Column("location", String(length=64), nullable=False)
    phone_number: str = Column(
        "phone_number", String(length=16), nullable=False
    )

    animals = relation("Animal", back_populates="shelters")
