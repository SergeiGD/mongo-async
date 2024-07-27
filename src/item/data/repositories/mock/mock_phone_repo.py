from typing import Optional

from src.item.data.repositories.mock.consts import MOCK_PHONE_DATA
from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import PhoneRequestData, IPhoneRepository


class MockPhoneRepository(IPhoneRepository):
    async def get_phones(self) -> list[Phone]:
        return [
            Phone(**MOCK_PHONE_DATA)
        ]
    
    async def create_phone(self, phone: PhoneRequestData) -> Phone:
        return Phone(
            name=phone.name,
            price=phone.price,
            description=phone.description,
            camera=phone.camera,
        )
    
    async def update_phone(self, phone_id: str, data: PhoneRequestData) -> Phone:
        return Phone(
            name=data.name,
            price=data.price,
            description=data.description,
            camera=data.camera,
        )
    
    async def get_phone(self, phone_id: str) -> Optional[Phone]:
        if id == MOCK_PHONE_DATA["id"]:
            Phone(**MOCK_PHONE_DATA)
