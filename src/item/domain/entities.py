from dataclasses import dataclass
from decimal import Decimal

from src.category.domain.entities import Category

@dataclass
class Item:
    id: str
    name: str
    price: Decimal
    description: str
    category: Category


@dataclass
class Phone(Item):
    id: str
    name: str
    price: Decimal
    description: str
    category: Category
    camera: int
    

@dataclass
class Laptop(Item):
    id: str
    name: str
    price: Decimal
    description: str
    category: Category
    ram: int
