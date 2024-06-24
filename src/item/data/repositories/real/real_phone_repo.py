from abc import ABC, abstractclassmethod

from src.item.data.mappers import map_phone
from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import CreatePhoneRequest, IPhoneRepository

from motor.motor_asyncio import AsyncIOMotorClient


class MongoPhoneRepository(IPhoneRepository):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_phones(self) -> list[Phone]:
        return [map_phone(phone) async for phone in self._client.db.items.find()]
        
    
    async def create_phone(self, phone: CreatePhoneRequest) -> Phone:
        raw_phone = await self._client.items.insert_one(phone)
        return map_phone(raw_phone)
    