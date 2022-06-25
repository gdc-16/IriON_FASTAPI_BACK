from datetime import datetime, timedelta

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.model import Animal, Shelter
from src.schema import CreateAnimal, UpdaetAnimal


class CRUDAnimal(CRUDBase[Animal, CreateAnimal, UpdaetAnimal]):
    async def get_by_id(self, db: Session, id: int) -> dict | None:
        query = select(self.model, Shelter).join(Shelter).where(
            self.model.id == id
        )
        instance = await db.execute(query)
        result =  jsonable_encoder(instance.fetchone())

        result["Animal"]["left_day"] = 510 - (
            datetime.today() - datetime.strptime(
                result["Animal"]["started_date"], "%Y-%m-%dT%H:%M:%S"
            )
        ).days
        return result

    async def get_multi(
        self, db: Session, offset: int, limit: int
    ) -> list | None:
        query = select(self.model)
        instances = await db.execute(query)
        result = jsonable_encoder(instances.scalars().all())

        data_size = len(result)
        data = result[offset:limit]

        for dict in data:
            dict["left_day"] = 510 - (
                datetime.today() - datetime.strptime(
                    dict["started_date"], "%Y-%m-%dT%H:%M:%S"
                )
        ).days

        return {
            "data": data,
            "size": data_size
        }


animal_crud = CRUDAnimal(model=Animal)
