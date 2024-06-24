from dataclasses import dataclass
import decimal
from typing import Protocol

@dataclass
class ItemProtocol(Protocol):
    name: str
    price: decimal
    description: str
    # category: Category


@dataclass
class Phone:
    name: str
    price: decimal
    description: str
    camera: int
    # category: Category


@dataclass
class Laptop:
    name: str
    price: decimal
    description: str
    ram: int
    # category: Category
