from bson import Decimal128
from src.item.domain.entities import Phone
from src.item.domain.repositories.phone_repo import CreatePhoneRequest


def map_phone(phone: dict) -> Phone:
    return Phone(
        name=phone["name"],
        price=phone["price"].to_decimal(),
        description=phone["description"],
        camera=phone["camera"],
    )

def map_create_phone_request_to_mongo_dict(request: CreatePhoneRequest) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "camera": request.camera,
    }