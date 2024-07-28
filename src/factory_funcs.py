from typing import Annotated
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.category.data.repositories.mock.mock_category_repo import MockCategoryRepository
from src.category.data.repositories.real.real_category_repo import MongoCategoryRepository
from src.category.domain.interactors.category_interactor import CategoryInteractor
from src.category.domain.repositories.category_repo import ICategoryRepository
from src.item.data.repositories.mock.mock_phone_repo import MockPhoneRepository
from src.item.data.repositories.mock.mock_laptop_repo import MockLaptopRepository
from src.item.data.repositories.mock.mock_item_repo import MockItemRepository
from src.item.data.repositories.real.real_item_repo import MongoItemRepository
from src.item.data.repositories.real.real_phone_repo import MongoPhoneRepository
from src.item.data.repositories.real.real_laptop_repo import MongoLaptopRepository
from src.item.domain.interactors.item_interactor import ItemInteractor, PhoneInteractor, LaptopInteractor
from src.item.domain.repositories.item_repo import IItemRepository
from src.item.domain.repositories.phone_repo import IPhoneRepository
from src.item.domain.repositories.laptop_repo import ILaptopRepository

from src.settings import settings, use_mock_settings


def get_async_client() -> AsyncIOMotorClient:
    uri = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_URI}"
    return AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    

def category_repository_factory(
    client: Annotated[AsyncIOMotorClient, Depends(get_async_client)]
) -> IItemRepository:
    if use_mock_settings.USE_MOCK_CATEGORY_REPO:
        return MockCategoryRepository()
    return MongoCategoryRepository(client)

def category_interactor_factory(
    category_repo: Annotated[ICategoryRepository, Depends(category_repository_factory)],
):
    return CategoryInteractor(category_repo)


def phone_repository_factory(
    client: Annotated[AsyncIOMotorClient, Depends(get_async_client)]
) -> IPhoneRepository:
    if use_mock_settings.USE_MOCK_PHONE_REPO:
        return MockPhoneRepository()
    return MongoPhoneRepository(client)


def laptop_repository_factory(
    client: Annotated[AsyncIOMotorClient, Depends(get_async_client)]
) -> ILaptopRepository:
    if use_mock_settings.USE_MOCK_PHONE_REPO:
        return MockLaptopRepository()
    return MongoLaptopRepository(client)


def item_repository_factory(
    client: Annotated[AsyncIOMotorClient, Depends(get_async_client)]
) -> IItemRepository:
    if use_mock_settings.USE_MOCK_ITEM_REPO:
        return MockItemRepository()
    return MongoItemRepository(client)


def phone_interactor_factory(
    phone_repo: Annotated[IPhoneRepository, Depends(phone_repository_factory)],
    category_repo: Annotated[ICategoryRepository, Depends(category_repository_factory)],
) -> PhoneInteractor:
    return PhoneInteractor(phone_repo=phone_repo, category_repo=category_repo)


def laptop_interactor_factory(
    laptop_repo: Annotated[ILaptopRepository, Depends(laptop_repository_factory)],
    category_repo: Annotated[ICategoryRepository, Depends(category_repository_factory)],
) -> LaptopInteractor:
    return LaptopInteractor(laptop_repo=laptop_repo, category_repo=category_repo)


def item_interactor_factory(
    item_repo: Annotated[IItemRepository, Depends(item_repository_factory)],
) -> ItemInteractor:
    return ItemInteractor(item_repo)
