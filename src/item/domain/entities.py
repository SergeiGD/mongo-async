from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol

@dataclass
class Item:
    name: str
    price: Decimal
    description: str
    category_key: str


@dataclass
class Phone(Item):
    name: str
    price: Decimal
    description: str
    category_key: str
    camera: int
    

@dataclass
class Laptop(Item):
    name: str
    price: Decimal
    description: str
    category_key: str
    ram: int


