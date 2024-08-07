from typing import Optional
from src.category.data.mappers import map_category
from src.category.domain.entities import Category
from motor.motor_asyncio import AsyncIOMotorClient

from src.category.domain.repositories.category_repo import ICategoryRepository


class MongoCategoryRepository(ICategoryRepository):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_categories(self) -> list[Category]:
        return [map_category(ategory) async for ategory in self._client.db.categories.find()]
        
    async def get_category_by_key(self, key: str) -> Optional[Category]:
        result = await self._client.db.categories.find_one(
            {
                "key": key,
            }
        )
        if result is not None:
            return map_category(result)
    