from abc import ABC, abstractclassmethod

from src.item.domain.entities import Laptop
from src.item.domain.repositories.laptop_repo import CreateLaptopRequest, ILaptopRepository


class MockLaptopRepository(ILaptopRepository):
    async def get_laptops(self) -> list[Laptop]:
        return [
            Laptop(
                name="thinkpad V",
                price=99999,
                description="Lorem ipsum",
                ram=24,
            )
        ]
    
    async def create_phone(self, laptop: CreateLaptopRequest) -> Laptop:
        return Laptop(
            name=laptop.name,
            price=laptop.price,
            description=laptop.description,
            ram=laptop.ram,
        )
    