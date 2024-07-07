from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol
from uuid import UUID

@dataclass
class Item:
    id: str
    name: str
    price: Decimal
    description: str
    category_key: str


@dataclass
class Phone(Item):
    id: str
    name: str
    price: Decimal
    description: str
    category_key: str
    camera: int
    

@dataclass
class Laptop(Item):
    id: str
    name: str
    price: Decimal
    description: str
    category_key: str
    ram: int
