from typing import Optional

from pymongo import ReturnDocument
from src.item.data.mappers import map_phone, map_phone_request_data_to_mongo_dict
from src.item.domain.consts import CategoriesKeys
from src.item.domain.entities import Phone
from src.item.domain.repositories.exceptions import NotFoundException, SaveException, SchemaException
from src.item.domain.repositories.phone_repo import PhoneRequestData, IPhoneRepository

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from bson.errors import BSONError


class MongoPhoneRepository(IPhoneRepository):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_phones(self) -> list[Phone]:
        return [map_phone(phone) async for phone in self._client.db.items.find(
            {"category_key": CategoriesKeys.PHONE.value}
        )]
        
    
    async def create_phone(self, phone: PhoneRequestData) -> Phone:
        result = await self._client.db.items.insert_one(map_phone_request_data_to_mongo_dict(phone))
        return map_phone(await self._client.db.items.find_one({"_id": result.inserted_id}))
    
    async def update_phone(self, phone_id: str, data: PhoneRequestData) -> Phone:
        try:
            result = await self._client.db.items.find_one_and_update(
                {
                    "category_key": CategoriesKeys.PHONE.value,
                    "_id": ObjectId(phone_id),
                },
                {"$set": map_phone_request_data_to_mongo_dict(data)},
                return_document=ReturnDocument.AFTER,
            )
        except BSONError:
            raise SchemaException
        if result is None:
            raise NotFoundException
        
        
        return map_phone(result)
    
    async def get_phone(self, phone_id: str) -> Optional[Phone]:
        result = await self._client.db.items.find_one(
            {
                "category_key": CategoriesKeys.PHONE.value,
                "_id": ObjectId(phone_id),
            }
        )
        if result is not None:
            return map_phone(result)
    