from sqlalchemy import Column, Integer, ForeignKey

from src.database import Base


class Follow(Base):
    follow: int = Column("follow", Integer, default=1)
    user_id: int = Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE")
    )
    animal_id: int = Column("animal_id", Integer, ForeignKey(
        "animals.id", ondelete="CASCADE"
    ))
