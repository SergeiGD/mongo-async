from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID


from src.item.domain.entities import Phone


@dataclass
class PhoneRequestData:
    name: str
    price: Decimal
    description: str
    camera: int
    category_key: str

class IPhoneRepository(ABC):
    @abstractclassmethod
    async def get_phones(self) -> list[Phone]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_phone(self, phone: PhoneRequestData) -> Phone:
        raise NotImplementedError
    
    @abstractclassmethod
    async def update_phone(self, phone_id: str, data: PhoneRequestData) -> Phone:
        raise NotImplementedError
    
    @abstractclassmethod
    async def get_phone(self, phone_id: str) -> Optional[Phone]:
        raise NotImplementedError