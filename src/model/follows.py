from email.policy import default
from sqlalchemy import Column, Integer, ForeignKey, Boolean

from src.database import Base


class Follow(Base):
    id: int = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    follow: bool = Column("follow", Boolean, default=True)
    user_id: int = Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE")
    )
    animal_id: int = Column("animal_id", Integer, ForeignKey(
        "animals.id", ondelete="CASCADE"
    ))
