from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.crud import animal_crud
from src.schema import (
    CreateAnimal,
    UpdaetAnimal,
)


SINGULAR_PREFIX = "animal"
PLURAL_PREFIX = "animals"


router = APIRouter()

@router.get(path=f"/{SINGULAR_PREFIX}" + "/{animal_id}")
async def get_animal(animal_id: int) -> JSONResponse:
    try:
        if result := await animal_crud.get_by_id(id=animal_id):
            return JSONResponse(
                content={"content": result},
                status_code=status.HTTP_200_OK,
            )
        
        else:
            return JSONResponse(
                content={"content": []},
                status_code=status.HTTP_404_NOT_FOUND,
            )

    except Exception as error:
        return JSONResponse(
            content={"content": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@router.post(path=f"/{SINGULAR_PREFIX}")
async def create_animal(insert_data: CreateAnimal) -> JSONResponse:
    try:
        await animal_crud.create(obj_in=insert_data)
        return JSONResponse(
            content={"content": "Success"},
            status_code=status.HTTP_200_OK,
        )

    except Exception as error:
        return JSONResponse(
            content={"content": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
