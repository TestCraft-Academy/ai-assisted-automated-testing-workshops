"""Demo 01: a plausible suggested check passes but misses the real rule."""

from decimal import Decimal

from shop import Item, delivery_charge

def main() -> None:
    # The suggested check covers only eligible goods at the £50 threshold.
    # Passing this assertion does not establish how gift cards are handled.
    suggested = delivery_charge([Item(Decimal("50"))])
    assert suggested == Decimal("0")
    print("[SCRIPTED AI-STYLE CHECK] £50 goods -> free delivery: PASS")

    # Gift cards do not count towards the threshold: £40 of eligible goods
    # requires £5 delivery. The flawed calculator includes the £10 gift card.
    actual = delivery_charge([Item(Decimal("40")), Item(Decimal("10"), gift_card=True)])
    expected = Decimal("5")
    # Report the mismatch without asserting so the example completes despite
    # the intentional defect in the delivery calculator.
    print(f"[MISSING EXAMPLE] £40 goods + £10 gift card -> expected £{expected}, got £{actual}")
    print("[DEFECT] Gift cards incorrectly count towards the free-delivery threshold.")
    print("[REVIEW QUESTION] Who agreed that gift cards do not count?")


# Avoid running the example when this module is imported.
if __name__ == "__main__":
    main()