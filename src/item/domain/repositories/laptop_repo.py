from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal


from src.item.domain.entities import Laptop


@dataclass
class LaptopRequestData:
    name: str
    price: Decimal
    description: str
    ram: int
    category_key: str

class ILaptopRepository(ABC):
    @abstractclassmethod
    async def get_laptops(self) -> list[Laptop]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_laptop(self, phone: LaptopRequestData) -> Laptop:
        raise NotImplementedError
    