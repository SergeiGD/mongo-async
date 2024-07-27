from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Path, HTTPException

from src.category.domain.entities import Category
from src.category.domain.interactors.category_interactor import CategoryInteractor
from src.factory_funcs import category_interactor_factory


router = APIRouter()


@router.get("/categories")
async def get_categories(
    category_interactor: Annotated[CategoryInteractor, Depends(category_interactor_factory)]
) -> list[Category]:
    return await category_interactor.get_categories()

