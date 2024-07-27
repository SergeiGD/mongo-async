from enum import Enum

class CategoriesKeys(str, Enum):
    PHONE = "phone"
    LAPTOP = "laptop"


CATEGORIES_NAMES = {
    CategoriesKeys.PHONE.value: "телефоны",
    CategoriesKeys.LAPTOP.value: "ноутбуки",
}
