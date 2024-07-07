import decimal
from uuid import UUID
from src.item.domain.consts import CategoriesKeys
from src.item.domain.entities import Phone, Laptop
from src.item.domain.repositories.item_repo import IItemRepository
from src.item.domain.repositories.phone_repo import PhoneRequestData, IPhoneRepository
from src.item.domain.repositories.laptop_repo import LaptopRequestData, ILaptopRepository


class PhoneInteractor:
    def __init__(
        self,
        phone_repo: IPhoneRepository,
    ) -> None:
        self._phone_repo = phone_repo

    async def get_phones(self) -> list[Phone]:
        return await self._phone_repo.get_phones()
    
    async def create_phone(
        self,
        name: str,
        price: decimal,
        description: str,
        camera: int,
    ) -> Phone:
        return await self._phone_repo.create_phone(
            PhoneRequestData(
                name=name,
                price=price,
                description=description,
                category_key=CategoriesKeys.PHONE.value,
                camera=camera,
            )
        )
    
    async def update_phone(
        self, 
        phone_id: str,
        name: str,
        price: decimal,
        description: str,
        camera: int,
    ):
        return await self._phone_repo.update_phone(
            phone_id,
            PhoneRequestData(
                name=name,
                price=price,
                description=description,
                category_key=CategoriesKeys.PHONE.value,
                camera=camera,
            )
        )
    
    async def get_phone(
        self, 
        phone_id: str,
    ):
        return await self._phone_repo.get_phone(phone_id)
    
    
class LaptopInteractor:
    def __init__(
        self,
        latop_repo: ILaptopRepository,
    ) -> None:
        self._latop_repo = latop_repo

    async def get_laptops(self) -> list[Laptop]:
        return await self._latop_repo.get_laptops()
    
    async def create_laptop(
        self,
        name: str,
        price: decimal,
        description: str,
        ram: int,
    ) -> Phone:
        return await self._latop_repo.create_laptop(
            LaptopRequestData(
                name=name,
                price=price,
                description=description,
                category_key=CategoriesKeys.LAPTOP.value,
                ram=ram,
            )
        )


class ItemInteractor:
    
    def __init__(
        self,
        item_repo: IItemRepository,
    ) -> None:
        self._item_repo = item_repo

    async def get_items(self):
        return await self._item_repo.get_items()
