from src.crud.base import CRUDBase
from src.model import Shelter
from src.schema import CraeteShelter, UpdateShelter


class CRUDShelter(CRUDBase[Shelter, CraeteShelter, UpdateShelter]):
    pass


shelter_crud = CRUDShelter(model=Shelter)
