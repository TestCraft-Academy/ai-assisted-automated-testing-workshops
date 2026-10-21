"""Fictional delivery calculator with a deliberate threshold defect."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable


@dataclass(frozen=True)
class Item:
    price: Decimal
    gift_card: bool = False


def delivery_charge(items: Iterable[Item]) -> Decimal:
    """Return delivery charge; BUG: gift cards count towards free delivery."""
    total = sum((item.price for item in items), Decimal("0"))
    return Decimal("0") if total >= Decimal("50") else Decimal("5")