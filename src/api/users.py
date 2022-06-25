from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


SINGULAR_PREFIX = "user"
PLURAL_PREFIX = "users"


router = APIRouter()

