import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from pymongo import IndexModel, ASCENDING, DESCENDING
from settings import settings
from category.domain.consts import CategoriesKeys, CATEGORIES_NAMES

async def main():
    """
    Создание индексов БД и загрузка фикстур
    """
    uri = f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_URI}"
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

    # setup indexes
    await client.db.items.create_index([
        ("category.key", ASCENDING),
    ])
    
    await client.db.categories.create_index([
        ("key", ASCENDING), 
    ], unique=True)

    # setup fixtures
    category_setup_tasks = []
    for category in CategoriesKeys:
        category_setup_tasks.append(
            client.db.categories.update_one(
                {"key": category.value, "name": CATEGORIES_NAMES.get(category.value, "")},
                {"$set": {"key": category.value, "name": CATEGORIES_NAMES.get(category.value, "")}},
                upsert=True,
            )
        )
    await asyncio.gather(*category_setup_tasks)


if __name__ == "__main__":
    asyncio.run(main())
