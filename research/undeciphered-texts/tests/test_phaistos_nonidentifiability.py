import importlib.util
import math
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "phaistos_nonidentifiability.py"
SPEC = importlib.util.spec_from_file_location("phaistos_nonidentifiability", SCRIPT)
assert SPEC and SPEC.loader
phaistos = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(phaistos)


class NonidentifiabilityTests(unittest.TestCase):
    def test_unanchored_phaistos_bound_is_45_factorial(self):
        self.assertEqual(phaistos.equivalent_mapping_count(45), math.factorial(45))
        self.assertEqual(math.factorial(45), 119622220865480194561963161495657715064383733760000000000)

    def test_anchor_reduces_permutation_space(self):
        self.assertEqual(phaistos.equivalent_mapping_count(45, 36), math.factorial(9))

    def test_36_anchors_are_needed_to_drop_below_one_million(self):
        self.assertEqual(phaistos.minimum_anchors_for_limit(45, 1_000_000), 36)
        self.assertGreater(phaistos.equivalent_mapping_count(45, 35), 1_000_000)
        self.assertLessEqual(phaistos.equivalent_mapping_count(45, 36), 1_000_000)

    def test_invalid_arguments_are_rejected(self):
        for signs, anchors in [(0, 0), (45, -1), (45, 46)]:
            with self.subTest(signs=signs, anchors=anchors):
                with self.assertRaises(ValueError):
                    phaistos.equivalent_mapping_count(signs, anchors)
        with self.assertRaises(ValueError):
            phaistos.minimum_anchors_for_limit(45, 0)


if __name__ == "__main__":
    unittest.main()
