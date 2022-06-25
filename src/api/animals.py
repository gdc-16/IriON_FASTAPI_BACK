from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


SINGULAR_PREFIX = "animal"
PLURAL_PREFIX = "animals"


router = APIRouter()

