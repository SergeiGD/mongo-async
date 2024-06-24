from typing import Annotated
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.item.data.repositories.mock.mock_phone_repo import MockPhoneRepository
from src.item.data.repositories.real.real_phone_repo import MongoPhoneRepository
from src.item.domain.interactors.phone_interactor import PhoneInteractor
from src.item.domain.repositories.phone_repo import IPhoneRepository


def get_async_client() -> AsyncIOMotorClient:
    # uri = settings.MONGO_URI
    uri = "catalog_db:27017"
    return AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    

def phone_repository_factory(
    client: Annotated[AsyncIOMotorClient, Depends(get_async_client)]
) -> IPhoneRepository:
    # if settings.USE_MOCK_PHONES_REPO:
        # return MockPhoneRepository()
    return MongoPhoneRepository(client)

def phone_interactor_factory(
    phone_repo: Annotated[IPhoneRepository, Depends(phone_repository_factory)]
) -> PhoneInteractor:
    return PhoneInteractor(phone_repo)
