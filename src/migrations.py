import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from settings import settings

async def main():
    """
    Создание индексов БД
    """
    uri = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_URI}"
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

    await client.db.items.create_index("category_key")


if __name__ == "__main__":
    asyncio.run(main())
