from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: int = Column('id', Integer, primary_key=True, autoincrement=True)
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'
        