from fastapi import APIRouter, status, Depends, Query
from fastapi.responses import JSONResponse

from src.crud import animal_crud
from src.schema import (
    CreateAnimal,
    UpdaetAnimal,
)
from src.database import get_db


SINGULAR_PREFIX = "animal"
PLURAL_PREFIX = "animals"


router = APIRouter()

@router.get(path=f"/{SINGULAR_PREFIX}" + "/{animal_id}")
async def get_animal(animal_id: int, db=Depends(get_db)) -> JSONResponse:
    try:
        if result := await animal_crud.get_by_id(id=animal_id, db=db):
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

@router.get(path=f"/{PLURAL_PREFIX}")
async def get_animals(
    db=Depends(get_db),
    offset: int = Query(default=0),
    limit: int = Query(default=0),
) -> JSONResponse:
    try:
        if result := await animal_crud.get_multi(
            db=db, offset=offset, limit=limit
        ):
            return JSONResponse(
                content={"content": result},
                status_code=status.HTTP_200_OK
            )

        else:
            return JSONResponse(
                content={"content": []},
                status_code=status.HTTP_404_NOT_FOUND
            )

    except Exception as error:
        return JSONResponse(
            content={"contetn": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.post(path=f"/{SINGULAR_PREFIX}")
async def create_animal(
    insert_data: CreateAnimal,
    db=Depends(get_db)
) -> JSONResponse:
    try:
        await animal_crud.create(db=db, obj_in=insert_data)
        return JSONResponse(
            content={"content": "Success"},
            status_code=status.HTTP_200_OK,
        )

    except Exception as error:
        return JSONResponse(
            content={"content": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
