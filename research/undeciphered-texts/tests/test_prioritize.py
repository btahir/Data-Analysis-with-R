import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "prioritize.py"
SPEC = importlib.util.spec_from_file_location("prioritize", SCRIPT)
assert SPEC and SPEC.loader
prioritize = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prioritize)


class PrioritizeTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.path = Path(self.temp_dir.name) / "candidates.csv"

    def write_rows(self, rows):
        fields = ["id", "name", *prioritize.SCORE_COLUMNS, "score_total", "verdict"]
        with self.path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_ranking_uses_total_then_name(self):
        self.write_rows(
            [
                dict(id="b", name="Beta", score_data=1, score_anchor=1,
                     score_structure=1, score_validation=0, score_total=3, verdict="x"),
                dict(id="z", name="Zulu", score_data=1, score_anchor=1,
                     score_structure=0, score_validation=0, score_total=2, verdict="x"),
                dict(id="a", name="Alpha", score_data=0, score_anchor=1,
                     score_structure=1, score_validation=1, score_total=3, verdict="x"),
            ]
        )
        rows = prioritize.rank_candidates(prioritize.load_candidates(self.path))
        self.assertEqual([row["id"] for row in rows], ["a", "b", "z"])

    def test_rejects_incorrect_total(self):
        self.write_rows(
            [dict(id="a", name="Alpha", score_data=1, score_anchor=1,
                  score_structure=1, score_validation=1, score_total=99, verdict="x")]
        )
        with self.assertRaisesRegex(ValueError, "expected 4"):
            prioritize.load_candidates(self.path)

    def test_rejects_duplicate_id(self):
        row = dict(id="same", name="Alpha", score_data=1, score_anchor=1,
                   score_structure=1, score_validation=1, score_total=4, verdict="x")
        self.write_rows([row, row])
        with self.assertRaisesRegex(ValueError, "duplicate id"):
            prioritize.load_candidates(self.path)

    def test_rejects_out_of_range_component(self):
        self.write_rows(
            [dict(id="a", name="Alpha", score_data=4, score_anchor=0,
                  score_structure=0, score_validation=0, score_total=4, verdict="x")]
        )
        with self.assertRaisesRegex(ValueError, "must be 0–3"):
            prioritize.load_candidates(self.path)


if __name__ == "__main__":
    unittest.main()
