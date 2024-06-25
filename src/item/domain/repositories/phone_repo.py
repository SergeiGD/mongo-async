from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from decimal import Decimal


from src.item.domain.entities import Phone


@dataclass
class CreatePhoneRequest:
    name: str
    price: Decimal
    description: str
    camera: int
    # category_key: str

class IPhoneRepository(ABC):
    @abstractclassmethod
    async def get_phones(self) -> list[Phone]:
        raise NotImplementedError
    
    @abstractclassmethod
    async def create_phone(self, phone: CreatePhoneRequest) -> Phone:
        raise NotImplementedError
    