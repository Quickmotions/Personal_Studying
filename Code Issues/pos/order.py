from dataclasses import dataclass, field
from enum import auto, Enum

from pos.line_item import LineItem


class OrderStatus(Enum):
    """Order status"""

    OPEN = auto()
    PAID = auto()
    CANCELLED = auto()
    DELIVERED = auto()
    RETURNED = auto()


@dataclass
class Order:

    # --------
    # ISSUE: before

    # customer_id: int = 0
    # customer_name: str = ""
    # customer_address: str = ""
    # customer_postal_code: str = ""
    # customer_city: str = ""
    # customer_email: str = ""

    # after: (add customer class so that order has less responsibilities)
    # TODO: COMPLETE this https://youtu.be/Kl3_Gmn4Ujg?t=773
    # ---------

    # ---------
    # ISSUE: before

    # items: list[str] = field(default_factory=list)
    # quantities: list[int] = field(default_factory=list)
    # prices: list[int] = field(default_factory=list)

    # after: (introduce LineItem)
    items: list[LineItem] = field(default_factory=list)
    # ---------

    _status: OrderStatus = OrderStatus.OPEN

    def create_line_item(self, item: LineItem) -> None:
        self.items.append(item)

    def set_status(self, status: OrderStatus):
        self._status = status
