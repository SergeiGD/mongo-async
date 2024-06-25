from typing import Annotated

from fastapi import APIRouter, Depends

from src.item.domain.entities import Phone
from src.item.domain.interactors.phone_interactor import PhoneInteractor
from src.item.presentation.schemas import CreatePhoneSchema
from src.factory_funcs import phone_interactor_factory

router = APIRouter()


@router.get("/phones")
async def get_phones(
    phones_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)]
) -> list[Phone]:
    return await phones_interactor.get_phones()


@router.post("/phones")
async def add_phone(
    phones_interactor: Annotated[PhoneInteractor, Depends(phone_interactor_factory)],
    request: CreatePhoneSchema,
) -> Phone:
    return await phones_interactor.create_phone(
        name=request.name,
        price=request.price,
        description=request.description,
        camera=request.camera,
    )
