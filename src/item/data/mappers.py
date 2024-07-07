from bson import Decimal128
from src.item.domain.entities import Phone, Laptop
from src.item.domain.repositories.phone_repo import PhoneRequestData
from src.item.domain.repositories.laptop_repo import LaptopRequestData


def map_phone(phone: dict) -> Phone:
    return Phone(
        id=str(phone["_id"]),
        name=phone["name"],
        price=phone["price"].to_decimal(),
        description=phone["description"],
        category_key=phone["category_key"],
        camera=phone["camera"],
    )

def map_phone_request_data_to_mongo_dict(request: PhoneRequestData) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "category_key": request.category_key,
        "camera": request.camera,
    }

def map_laptop(laptop: dict) -> Laptop:
    return Laptop(
        id=str(laptop["_id"]),
        name=laptop["name"],
        price=laptop["price"].to_decimal(),
        description=laptop["description"],
        category_key=laptop["category_key"],
        ram=laptop["ram"],
    )

def map_create_laptop_request_to_mongo_dict(request: LaptopRequestData) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "category_key": request.category_key,
        "ram": request.ram,
    }