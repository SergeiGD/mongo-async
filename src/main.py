from typing import Annotated, Union

from fastapi import Depends, FastAPI, Request

from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.item.domain.repositories.exceptions import UnknownCategoryException
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

@app.exception_handler(UnknownCategoryException)
async def unknown_service_exception_handler(request: Request, exc: UnknownCategoryException):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )
