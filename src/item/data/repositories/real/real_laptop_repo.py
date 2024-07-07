from src.item.data.mappers import map_laptop, map_create_laptop_request_to_mongo_dict
from src.item.domain.consts import CategoriesKeys
from src.item.domain.entities import Laptop
from src.item.domain.repositories.laptop_repo import LaptopRequestData, ILaptopRepository

from motor.motor_asyncio import AsyncIOMotorClient


class MongoLaptopRepository(ILaptopRepository):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_laptops(self) -> list[Laptop]:
        return [map_laptop(laptop) async for laptop in self._client.db.items.find(
            {"category_key": CategoriesKeys.LAPTOP.value}
        )]
        
    
    async def create_laptop(self, laptop: LaptopRequestData) -> Laptop:
        result = await self._client.db.items.insert_one(map_create_laptop_request_to_mongo_dict(laptop))
        return map_laptop(await self._client.db.items.find_one({"_id": result.inserted_id}))
    