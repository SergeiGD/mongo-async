from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID


from src.category.domain.entities import Category
from src.item.domain.entities import Phone


@dataclass
class PhoneCreateRequestData:
    name: str
    price: Decimal
    description: str
    camera: int
    category: Category

@dataclass
class PhoneUpdateRequestData:
    name: str
    price: Decimal
    description: str
    camera: int

class IPhoneRepository(ABC):
    @abstractclassmethod
    async def get_phones(self) -> list[Phone]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_phone(self, phone: PhoneCreateRequestData) -> Phone:
        raise NotImplementedError
    
    @abstractclassmethod
    async def update_phone(self, phone_id: str, data: PhoneUpdateRequestData) -> Phone:
        raise NotImplementedError
    
    @abstractclassmethod
    async def get_phone(self, phone_id: str) -> Optional[Phone]:
        raise NotImplementedError