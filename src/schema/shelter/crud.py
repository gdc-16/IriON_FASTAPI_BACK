from src.schema.crud_base import CRUDSchemaBase


class ShelterBase(CRUDSchemaBase):
    name: str | None
    location: str | None
    phone_number: str | None


class CraeteShelter(ShelterBase):
    name: str
    location: str
    phone_number: str

    class Config:
        schema_extra: dict = {
            "example": {

            }
        }


class UpdateShelter(ShelterBase):
    pass
