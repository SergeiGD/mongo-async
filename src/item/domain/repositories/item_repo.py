from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal


from src.item.domain.entities import Item

class IItemRepository(ABC):
    @abstractclassmethod
    async def get_items(self) -> list[Item]:
        raise NotImplementedError
