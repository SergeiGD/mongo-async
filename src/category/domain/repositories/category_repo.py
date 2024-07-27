from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal

from src.category.domain.entities import Category




class ICategoryRepository(ABC):
    @abstractclassmethod
    async def get_categories(self) -> list[Category]:
        raise NotImplementedError
