from typing import Optional

from src.category.domain.consts import CategoriesKeys
from src.category.domain.entities import Category
from src.item.data.repositories.mock.consts import MOCK_PHONE_DATA
from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import PhoneCreateRequestData, IPhoneRepository, PhoneUpdateRequestData


class MockPhoneRepository(IPhoneRepository):
    async def get_phones(self) -> list[Phone]:
        return [
            Phone(**MOCK_PHONE_DATA)
        ]
    
    async def create_phone(self, phone: PhoneCreateRequestData) -> Phone:
        return Phone(
            name=phone.name,
            price=phone.price,
            description=phone.description,
            camera=phone.camera,
            category=Category(
                name="Телефоны",
                key=CategoriesKeys.PHONE.value,
            ),
        )
    
    async def update_phone(self, phone_id: str, data: PhoneUpdateRequestData) -> Phone:
        return Phone(
            name=data.name,
            price=data.price,
            description=data.description,
            camera=data.camera,
            category=Category(
                name="Телефоны",
                key=CategoriesKeys.PHONE.value,
            ),
        )
    
    async def get_phone(self, phone_id: str) -> Optional[Phone]:
        if id == MOCK_PHONE_DATA["id"]:
            Phone(**MOCK_PHONE_DATA)
