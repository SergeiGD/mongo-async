from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal


from src.category.domain.entities import Category
from src.item.domain.entities import Laptop


@dataclass
class LaptopCreateRequestData:
    name: str
    price: Decimal
    description: str
    ram: int
    category: Category

class ILaptopRepository(ABC):
    @abstractclassmethod
    async def get_laptops(self) -> list[Laptop]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_laptop(self, phone: LaptopCreateRequestData) -> Laptop:
        raise NotImplementedError
    