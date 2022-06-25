from pydantic import BaseModel


class CRUDSchemaBase(BaseModel):
    id: int
