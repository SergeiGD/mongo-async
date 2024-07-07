from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse

from src.item.domain.repositories.exceptions import UnknownCategoryException
from src.item.presentation.views import router as item_router

app = FastAPI()
    
    
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
