from pydantic import BaseModel


class FollowBase(BaseModel):
    follow: bool | None


class CreateFollow(FollowBase):
    user_id: int
    animal_id: int

    class Config:
        schema_extra: dict ={
            "example" : {

            }
        }


class UpdateFollow(FollowBase):
    follow: bool
