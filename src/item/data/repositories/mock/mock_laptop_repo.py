from abc import ABC, abstractclassmethod

from src.item.data.repositories.mock.consts import MOCK_LAPTOP_DATA
from src.item.domain.entities import Laptop
from src.item.domain.repositories.laptop_repo import LaptopRequestData, ILaptopRepository


class MockLaptopRepository(ILaptopRepository):
    async def get_laptops(self) -> list[Laptop]:
        return [
            Laptop(**MOCK_LAPTOP_DATA)
        ]
    
    async def create_phone(self, laptop: LaptopRequestData) -> Laptop:
        return Laptop(
            name=laptop.name,
            price=laptop.price,
            description=laptop.description,
            ram=laptop.ram,
        )
    