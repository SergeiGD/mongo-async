from typing import Annotated, Union

from fastapi import Depends, FastAPI

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.factory_funcs import phone_interactor_factory
from src.item.domain.interactors.phone_interactor import PhoneInteractor
from src.item.presentation.views import router as item_router

app = FastAPI()


@app.get("/")
async def read_root():
    uri = "catalog_db:27017"
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    try:
        await client.admin.command('ping')
        return {"ping": "pong"}
    except Exception as e:
        return {"ping": str(e)}
    
    
app.include_router(
    item_router,
    prefix="/items/v1",
    tags=["Items"],
)
