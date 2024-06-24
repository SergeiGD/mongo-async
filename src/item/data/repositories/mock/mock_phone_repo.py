from abc import ABC, abstractclassmethod

from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import CreatePhoneRequest, IPhoneRepository


class MockPhoneRepository(IPhoneRepository):
    async def get_phones(self) -> list[Phone]:
        return [
            Phone(
                name="pixel 6a",
                price=39999,
                description="Lorem ipsum",
                camera=48,
            )
        ]
    
    async def create_phone(self, phone: CreatePhoneRequest) -> Phone:
        return Phone(
            name=phone.name,
            price=phone.price,
            description=phone.description,
            camera=phone.camera,
        )
    