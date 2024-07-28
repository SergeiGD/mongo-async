import decimal
from uuid import UUID
from src.category.domain.consts import CategoriesKeys
from src.category.domain.entities import Category
from src.category.domain.exceptions import UnknownCategoryException
from src.category.domain.repositories.category_repo import ICategoryRepository
from src.item.domain.entities import Phone, Laptop
from src.item.domain.repositories.item_repo import IItemRepository
from src.item.domain.repositories.phone_repo import PhoneCreateRequestData, IPhoneRepository, PhoneUpdateRequestData
from src.item.domain.repositories.laptop_repo import LaptopCreateRequestData, ILaptopRepository


class PhoneInteractor:
    def __init__(
        self,
        phone_repo: IPhoneRepository,
        category_repo: ICategoryRepository,
    ) -> None:
        self._phone_repo = phone_repo
        self._category_repo = category_repo

    async def get_phones(self) -> list[Phone]:
        return await self._phone_repo.get_phones()
    
    async def create_phone(
        self,
        name: str,
        price: decimal,
        description: str,
        camera: int,
    ) -> Phone:
        category = await self._category_repo.get_category_by_key(CategoriesKeys.PHONE.value)
        if category is None:
            raise UnknownCategoryException
        return await self._phone_repo.create_phone(
            PhoneCreateRequestData(
                name=name,
                price=price,
                description=description,
                category=category,
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
            PhoneUpdateRequestData(
                name=name,
                price=price,
                description=description,
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
        laptop_repo: ILaptopRepository,
        category_repo: ICategoryRepository,
    ) -> None:
        self._laptop_repo = laptop_repo
        self._category_repo = category_repo

    async def get_laptops(self) -> list[Laptop]:
        return await self._laptop_repo.get_laptops()
    
    async def create_laptop(
        self,
        name: str,
        price: decimal,
        description: str,
        ram: int,
    ) -> Phone:
        category = await self._category_repo.get_category_by_key(CategoriesKeys.LAPTOP.value)
        if category is None:
            raise UnknownCategoryException
        
        return await self._laptop_repo.create_laptop(
            LaptopCreateRequestData(
                name=name,
                price=price,
                description=description,
                category=category,
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
