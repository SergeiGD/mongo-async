from src.category.domain.consts import CategoriesKeys
from src.item.data.mappers import map_phone, map_laptop
from src.item.domain.entities import Item
from src.item.domain.repositories.exceptions import UnknownCategoryException
from src.item.domain.repositories.item_repo import IItemRepository

from motor.motor_asyncio import AsyncIOMotorClient


class MongoItemRepository(IItemRepository):
    MAPPERS_MAP = {
        CategoriesKeys.PHONE.value: map_phone,
        CategoriesKeys.LAPTOP.value: map_laptop
    }

    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_items(self) -> list[Item]:
        items = [item async for item in self._client.db.items.find()]
        result = []
        for item in items:
            if mapper := self.MAPPERS_MAP.get(item.get("category", {}).get("key")):
                result.append(mapper(item))
            else:
                raise UnknownCategoryException
        return result
        
