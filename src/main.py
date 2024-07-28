from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse

from src.category.domain.exceptions import UnknownCategoryException
from src.common_exceptions import NotFoundException, SchemaException
from src.item.presentation.views import router as item_router
from src.category.presentation.views import router as category_router

app = FastAPI()
    
    
app.include_router(
    item_router,
    prefix="/items/v1",
    tags=["Items"],
)
app.include_router(
    category_router,
    prefix="/categories/v1",
    tags=["Categories"],
)

@app.exception_handler(UnknownCategoryException)
async def unknown_service_exception_handler(request: Request, exc: UnknownCategoryException):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )

@app.exception_handler(NotFoundException)
async def unknown_service_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exc.detail},
    )

@app.exception_handler(SchemaException)
async def unknown_service_exception_handler(request: Request, exc: SchemaException):
    return JSONResponse(
        status_code=400,
        content={"message": exc.detail},
    )
