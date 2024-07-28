from typing import Optional

from pymongo import ReturnDocument
from src.category.domain.consts import CategoriesKeys
from src.item.data.mappers import map_phone, map_phone_create_request_data_to_mongo_dict, map_phone_update_request_data_to_mongo_dict
from src.item.domain.entities import Phone
from src.common_exceptions import NotFoundException, SaveException, SchemaException
from src.item.domain.repositories.phone_repo import IPhoneRepository, PhoneCreateRequestData, PhoneUpdateRequestData

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from bson.errors import BSONError


class MongoPhoneRepository(IPhoneRepository):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self._client = client

    async def get_phones(self) -> list[Phone]:
        return [map_phone(phone) async for phone in self._client.db.items.find(
            {"category.key": CategoriesKeys.PHONE.value}
        )]
        
    
    async def create_phone(self, phone: PhoneCreateRequestData) -> Phone:
        insert_data = map_phone_create_request_data_to_mongo_dict(phone)
        result = await self._client.db.items.insert_one(insert_data)
        return map_phone(await self._client.db.items.find_one({"_id": result.inserted_id}))
    

    async def update_phone(self, phone_id: str, data: PhoneUpdateRequestData) -> Phone:
        try:
            result = await self._client.db.items.find_one_and_update(
                {
                    "category.key": CategoriesKeys.PHONE.value,
                    "_id": ObjectId(phone_id),
                },
                {"$set": map_phone_update_request_data_to_mongo_dict(data)},
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
                "category.key": CategoriesKeys.PHONE.value,
                "_id": ObjectId(phone_id),
            }
        )
        if result is not None:
            return map_phone(result)
    