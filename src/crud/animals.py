from src.crud.base import CRUDBase
from src.model import Animal
from src.schema import CreateAnimal, UpdaetAnimal


class CRUDAnimal(CRUDBase[Animal, CreateAnimal, UpdaetAnimal]):
    pass

animal_crud = CRUDAnimal(model=Animal)
