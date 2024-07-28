from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from src.category.domain.entities import Category




class ICategoryRepository(ABC):
    @abstractclassmethod
    async def get_categories(self) -> list[Category]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def get_category_by_key(self, key: str) -> Optional[Category]:
        raise NotImplementedError
