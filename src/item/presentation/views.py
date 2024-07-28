from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, HTTPException

from src.common_exceptions import NotFoundException
from src.item.domain.entities import Phone, Laptop
from src.item.domain.interactors.item_interactor import ItemInteractor, LaptopInteractor, PhoneInteractor
from src.item.presentation.schemas import CreateLaptopSchema, CreatePhoneSchema
from src.factory_funcs import item_interactor_factory, laptop_interactor_factory, phone_interactor_factory

router = APIRouter()


@router.get("/items")
async def get_items(
    item_interactor: Annotated[ItemInteractor, Depends(item_interactor_factory)]
) -> list[Phone | Laptop]:
    return await item_interactor.get_items()


@router.get("/phones")
async def get_phones(
    phone_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)]
) -> list[Phone]:
    return await phone_interactor.get_phones()


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


@router.put("/phones/{phone_id}")
async def update_phone(
    phone_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)],
    phone_id: Annotated[str, Path(min_length=24, max_length=24)],
    request: CreatePhoneSchema,
) -> Optional[Phone]:
    return await phone_interactor.update_phone(
        phone_id=phone_id,
        name=request.name,
        price=request.price,
        description=request.description,
        camera=request.camera,
    )


@router.get("/phones/{phone_id}")
async def get_phone(
    phone_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)],
    phone_id: Annotated[str, Path(min_length=24, max_length=24)],
) -> Optional[Phone]:
    result = await phone_interactor.get_phone(phone_id=phone_id)
    if result is None:
        raise NotFoundException
    return result


@router.get("/laptops")
async def get_laptops(
    laptop_interactor: Annotated[LaptopInteractor, Depends(laptop_interactor_factory)]
) -> list[Laptop]:
    return await laptop_interactor.get_laptops()


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
