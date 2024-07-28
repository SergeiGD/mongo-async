from src.category.domain.consts import CategoriesKeys
from src.category.domain.entities import Category
from src.item.data.repositories.mock.consts import MOCK_LAPTOP_DATA
from src.item.domain.entities import Laptop
from src.item.domain.repositories.laptop_repo import LaptopCreateRequestData, ILaptopRepository


class MockLaptopRepository(ILaptopRepository):
    async def get_laptops(self) -> list[Laptop]:
        return [
            Laptop(**MOCK_LAPTOP_DATA)
        ]
    
    async def create_phone(self, laptop: LaptopCreateRequestData) -> Laptop:
        return Laptop(
            name=laptop.name,
            price=laptop.price,
            description=laptop.description,
            category=Category(
                name="Ноутбуки",
                key=CategoriesKeys.LAPTOP.value,
            ),
            ram=laptop.ram,
        )
    