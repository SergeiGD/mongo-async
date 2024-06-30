from abc import ABC, abstractclassmethod

from src.item.domain.entities import Item, Phone, Laptop
from src.item.domain.repositories.item_repo import IItemRepository


class MockItemRepository(IItemRepository):
    async def get_items(self) -> list[Item]:
        return [
            Laptop(
                name="thinkpad V",
                price=99999,
                description="Lorem ipsum",
                ram=24,
            ),
            Phone(
                name="pixel 6a",
                price=39999,
                description="Lorem ipsum",
                camera=48,
            )
        ]
    