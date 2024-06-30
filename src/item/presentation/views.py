from typing import Annotated

from fastapi import APIRouter, Depends

from src.item.domain.entities import Item, Phone, Laptop
from src.item.domain.interactors.item_interactor import ItemInteractor, LaptopInteractor, PhoneInteractor
from src.item.presentation.schemas import CreateLaptopSchema, CreatePhoneSchema
from src.factory_funcs import item_interactor_factory, laptop_interactor_factory, phone_interactor_factory

router = APIRouter()


@router.get("/items")
async def get_phones(
    item_interactor: Annotated[ItemInteractor, Depends(item_interactor_factory)]
) -> list[Phone | Laptop]:
    return await item_interactor.get_items()


@router.post("/phones")
async def add_phone(
    phone_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)],
    request: CreatePhoneSchema,
) -> Phone:
    return await phone_interactor.create_phone(
        name=request.name,
        price=request.price,
        description=request.description,
        camera=request.camera,
    )

@router.post("/laptops")
async def add_laptop(
    laptop_interactor: Annotated[LaptopInteractor, Depends(laptop_interactor_factory)],
    request: CreateLaptopSchema,
) -> Laptop:
    return await laptop_interactor.create_laptop(
        name=request.name,
        price=request.price,
        description=request.description,
        ram=request.ram,
    )
