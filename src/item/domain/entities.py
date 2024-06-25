from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol

@dataclass
class ItemProtocol(Protocol):
    name: str
    price: Decimal
    description: str
    # category: Category


@dataclass
class Phone:
    name: str
    price: Decimal
    description: str
    camera: int
    # category: Category


@dataclass
class Laptop:
    name: str
    price: Decimal
    description: str
    ram: int
    # category: Category
