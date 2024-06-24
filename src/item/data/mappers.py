from src.item.domain.entities import Phone


def map_phone(phone: dict) -> Phone:
    return Phone(
        name=phone.name,
            price=phone["price"],
            description=phone["description"],
            camera=phone["camera"],
    )