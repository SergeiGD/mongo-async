from abc import ABC, abstractclassmethod

from src.item.domain.entities import Item, Phone, Laptop
from src.item.domain.repositories.item_repo import IItemRepository
from src.item.data.repositories.mock.consts import MOCK_PHONE_DATA, MOCK_LAPTOP_DATA


class MockItemRepository(IItemRepository):
    async def get_items(self) -> list[Item]:
        return [
            Laptop(**MOCK_PHONE_DATA),
            Phone(**MOCK_LAPTOP_DATA)
        ]
    