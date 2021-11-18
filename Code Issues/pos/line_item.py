from dataclasses import dataclass


@dataclass
class LineItem:
    item: str
    quantity: int
    price: int