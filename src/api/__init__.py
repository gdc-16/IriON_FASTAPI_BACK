from fastapi import APIRouter

from src.api import animals, users, shelters


router = APIRouter(prefix="/v1")

router.include_router(router=animals.router, tags=["유기동물"])
router.include_router(router=shelters.router, tags=["보호소"])
router.include_router(router=users.router, tags=["사용자"])
