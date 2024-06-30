from pydantic import BaseModel
from decimal import Decimal


class CreatePhoneSchema(BaseModel):
    name: str
    price: Decimal
    description: str
    camera: int

class CreateLaptopSchema(BaseModel):
    name: str
    price: Decimal
    description: str
    ram: int
