from typing import TypeVar, Generic, Type

from fastapi.encoders import jsonable_encoder
from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from src.database import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        model: Type[ModelType],
    ) -> None:
        self.model = model
        

    async def get_by_id(self, db: Session, id: int) -> dict | None:
        query = select(self.model).where(self.model.id == id)
        instance = await db.execute(query)
        result = instance.fetchone()
        return result

    
    async def get_multi(
        self,
        db: Session,
        offset: int,
        limit: int,
    ) -> list | None:
        query = select(self.model).offset(offset).limit(limit)
        instances = await db.execute(query)
        result = instances.scalars().all()
        return result

        
        
    async def create(self, db: Session, obj_in: CreateSchemaType) -> None:
        new_data = self.model(**jsonable_encoder(obj_in))
        db.add(new_data)
        await db.commit()
    
    
    async def update(self, db: Session, id: int, obj_update: UpdateSchemaType) -> None:
        query = update(
            self.model
        ).where(
            self.model.id == id
        ).values(**jsonable_encoder(obj_update))
        await db.execute(query)
        await db.commit()

        
    async def delete(self, db: Session, id: int) -> None:
        query = delete(self.model).where(self.model.id == id)
        await db.execute(query)
        await db.commit()
