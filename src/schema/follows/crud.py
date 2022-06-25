from src.schema.crud_base import CRUDSchemaBase


class FollowBase(CRUDSchemaBase):
    pass


class CreateFollow(FollowBase):
    user_id: int
    animal_id: int

    class Config:
        schema_extra: dict ={
            "example" : {

            }
        }


class UpdateFollow(FollowBase):
    pass
