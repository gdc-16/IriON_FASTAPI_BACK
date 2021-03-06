from email.policy import default
import enum

from sqlalchemy import Column, String, Enum, Boolean, Integer
from sqlalchemy.orm import relation

from src.database import Base


class UserType(str, enum.Enum):
    USER = "user"
    CHIEF = "chief"


class User(Base):
    id: int = Column("id", Integer, primary_key=True, autoincrement=True)
    name: str = Column("name", String(length=8), nullable=False)
    user_id: str = Column("user_id", String(length=16), nullable=False, unique=True)
    password: str = Column("password", String(length=256), nullable=False)
    role: UserType = Column("role", Enum(UserType))
    phone_number: str = Column("phone_number", String(length=16), nullable=False)
    certificate: bool = Column("certificate", Boolean(), default=False)
    
    animals = relation("Animal", secondary="follows", back_populates="users")

