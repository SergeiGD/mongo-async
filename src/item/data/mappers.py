from bson import Decimal128
from src.item.domain.entities import Phone, Laptop
from src.category.domain.entities import Category
from src.item.domain.repositories.phone_repo import PhoneCreateRequestData, PhoneUpdateRequestData
from src.item.domain.repositories.laptop_repo import LaptopCreateRequestData


def map_phone(phone: dict) -> Phone:
    return Phone(
        id=str(phone["_id"]),
        name=phone["name"],
        price=phone["price"].to_decimal(),
        description=phone["description"],
        category=Category(
            name=phone["category"]["name"],
            key=phone["category"]["key"]
        ),
        camera=phone["camera"],
    )

def map_phone_create_request_data_to_mongo_dict(request: PhoneCreateRequestData) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "category": {"key": request.category.key, "name": request.category.name},
        "camera": request.camera,
    }

def map_phone_update_request_data_to_mongo_dict(request: PhoneUpdateRequestData) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "camera": request.camera,
    }

def map_laptop(laptop: dict) -> Laptop:
    return Laptop(
        id=str(laptop["_id"]),
        name=laptop["name"],
        price=laptop["price"].to_decimal(),
        description=laptop["description"],
        category=Category(
            name=laptop["category"]["name"],
            key=laptop["category"]["key"]
        ),
        ram=laptop["ram"],
    )

def map_laptop_create_request_to_mongo_dict(request: LaptopCreateRequestData) -> dict:
    return {
        "name": request.name,
        "price": Decimal128(request.price),
        "description": request.description,
        "category": {"key": request.category.key, "name": request.category.name},
        "ram": request.ram,
    }