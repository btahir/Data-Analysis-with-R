#!/usr/bin/env python3
"""Validate and rank undeciphered-text research candidates.

This intentionally uses only Python's standard library.  The research workflow
does not need R, a plotting stack, or a package installation merely to validate
a CSV and sort four small integer scores.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


SCORE_COLUMNS = (
    "score_data",
    "score_anchor",
    "score_structure",
    "score_validation",
)
OUTPUT_COLUMNS = ("id", "name", *SCORE_COLUMNS, "score_total", "verdict")
REQUIRED_COLUMNS = {
    "id",
    "name",
    "score_total",
    "verdict",
    *SCORE_COLUMNS,
}


def load_candidates(path: Path) -> list[dict[str, str]]:
    """Load *path* and reject ambiguous or internally inconsistent rows."""
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path}: missing CSV header")

        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            raise ValueError(f"{path}: missing columns: {', '.join(sorted(missing))}")

        rows = list(reader)

    if not rows:
        raise ValueError(f"{path}: no candidate rows")

    seen_ids: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        if None in row:
            raise ValueError(f"{path}:{line_number}: too many CSV fields")

        candidate_id = row["id"].strip()
        if not candidate_id:
            raise ValueError(f"{path}:{line_number}: empty candidate id")
        if candidate_id in seen_ids:
            raise ValueError(f"{path}:{line_number}: duplicate id {candidate_id!r}")
        seen_ids.add(candidate_id)

        try:
            scores = [int(row[column]) for column in SCORE_COLUMNS]
            stated_total = int(row["score_total"])
        except ValueError as error:
            raise ValueError(
                f"{path}:{line_number}: scores must be integers"
            ) from error

        if any(score not in range(4) for score in scores):
            raise ValueError(f"{path}:{line_number}: component scores must be 0–3")
        if sum(scores) != stated_total:
            raise ValueError(
                f"{path}:{line_number}: score_total is {stated_total}, "
                f"expected {sum(scores)}"
            )

    return rows


def rank_candidates(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Return candidates by descending total, then stable alphabetical name."""
    return sorted(rows, key=lambda row: (-int(row["score_total"]), row["name"]))


def write_ranking(path: Path, rows: Iterable[dict[str, str]]) -> None:
    """Write the compact, reviewable ranking artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in OUTPUT_COLUMNS})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("research/undeciphered-texts/data/candidates.csv"),
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path("research/undeciphered-texts/outputs/ranking.csv"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = rank_candidates(load_candidates(args.input))
    write_ranking(args.output, rows)
    print(f"Wrote {len(rows)} ranked candidates to {args.output}")


if __name__ == "__main__":
    main()
