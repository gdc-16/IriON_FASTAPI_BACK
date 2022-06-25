import enum

from sqlalchemy import Column, String

from src.database import Base


class UserRole(str, enum.Enum):
    USER = "user"
    CHIEF = "chief"


class User(Base):
    name: str = Column("name", String())
    user_id: str
    password: str
    role: UserRole
    phone_number: str
    certificate: bool 
