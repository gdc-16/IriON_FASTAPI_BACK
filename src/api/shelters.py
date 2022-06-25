from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.crud import shelter_crud
from src.schema import (
    CraeteShelter,
    UpdateShelter,
)


SINGULAR_PREFIX = "shelter"
PLURAL_PREFIX = "shelters"

router = APIRouter()


@router.post(path=f"{SINGULAR_PREFIX}")
async def create_shelter(insert_data: CraeteShelter) -> JSONResponse:
    try:
        await shelter_crud.create(obj_in=insert_data)
        return JSONResponse(
            content={"content": "Success"},
            status_code=status.HTTP_200_OK,
        )
    
    except Exception as error:
        return JSONResponse(
            content={"content": str(error)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
        