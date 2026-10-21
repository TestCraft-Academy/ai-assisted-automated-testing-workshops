"""Keep the intentionally flawed example and simulated policy reproducible."""

import subprocess
import sys
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "demos"))
from policy import approve_tool  # noqa: E402
from shop import Item, delivery_charge  # noqa: E402


class WorkshopTests(unittest.TestCase):
    def test_suggested_happy_path_passes(self) -> None:
        self.assertEqual(delivery_charge([Item(Decimal("50"))]), Decimal("0"))

    def test_defect_is_still_visible(self) -> None:
        basket = [Item(Decimal("40")), Item(Decimal("10"), gift_card=True)]
        self.assertEqual(delivery_charge(basket), Decimal("0"))  # Intended rule: £5

    def test_below_threshold_costs_five(self) -> None:
        self.assertEqual(delivery_charge([Item(Decimal("40"))]), Decimal("5"))

    def test_tool_policy_denies_everything_except_empty_read(self) -> None:
        self.assertTrue(approve_tool("read_test_summary"))
        self.assertFalse(approve_tool("read_test_summary", "EXAMPLE_SECRET_DO_NOT_USE"))
        self.assertFalse(approve_tool("run_shell", "echo example"))
        self.assertFalse(approve_tool("write_file"))

    def test_all_demos_run_from_repository_root(self) -> None:
        for name, expected in (
            ("01_green_check.py", "expected £5, got £0"),
            ("02_review_selenium.py", "NOT EXECUTED"),
            ("03_agent_guardrails.py", "[DENY] secret in payload"),
        ):
            with self.subTest(name=name):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "demos" / name)],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertIn(expected, result.stdout)


if __name__ == "__main__":
    unittest.main()