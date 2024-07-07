from uuid import UUID
from pydantic import BaseModel, Field
from decimal import Decimal


class CreatePhoneSchema(BaseModel):
    name: str
    price: Decimal = Field(ge=999)
    description: str
    camera: int = Field(ge=8, le=64)

class CreateLaptopSchema(BaseModel):
    name: str
    price: Decimal = Field(ge=999)
    description: str
    ram: int = Field(ge=2, le=32)
