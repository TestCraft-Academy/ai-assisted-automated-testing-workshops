"""Demo 01: a plausible suggested check passes but misses the real rule."""

from decimal import Decimal

from shop import Item, delivery_charge


def main() -> None:
    suggested = delivery_charge([Item(Decimal("50"))])
    assert suggested == Decimal("0")
    print("[SCRIPTED AI-STYLE CHECK] £50 goods -> free delivery: PASS")

    actual = delivery_charge([Item(Decimal("40")), Item(Decimal("10"), gift_card=True)])
    expected = Decimal("5")
    print(f"[MISSING EXAMPLE] £40 goods + £10 gift card -> expected £{expected}, got £{actual}")
    print("[DEFECT] Gift cards incorrectly count towards the free-delivery threshold.")
    print("[REVIEW QUESTION] Who agreed that gift cards do not count?")


if __name__ == "__main__":
    main()