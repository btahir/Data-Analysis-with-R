#!/usr/bin/env python3
"""Quantify label non-identifiability for the Phaistos Disc.

The result is an exact combinatorial bound, not a proposed decipherment.  If a
model uses only intrinsic structure that is invariant to renaming signs, every
bijection from the unanchored signs to an equally sized label set has the same
fit.  With ``n`` signs and ``k`` externally anchored sign values, that equivalence
class contains ``(n-k)!`` mappings.
"""

from __future__ import annotations

import argparse
import json
import math


def equivalent_mapping_count(signs: int, anchors: int = 0) -> int:
    """Return the exact number of relabelings left after *anchors* are fixed."""
    if signs < 1:
        raise ValueError("signs must be positive")
    if anchors < 0 or anchors > signs:
        raise ValueError("anchors must be between zero and signs")
    return math.factorial(signs - anchors)


def minimum_anchors_for_limit(signs: int, limit: int) -> int:
    """Return how many fixed values reduce the equivalence class to ``limit``."""
    if limit < 1:
        raise ValueError("limit must be positive")
    for anchors in range(signs + 1):
        if equivalent_mapping_count(signs, anchors) <= limit:
            return anchors
    raise AssertionError("all signs anchored must leave exactly one mapping")


def result(signs: int, anchors: int, limit: int) -> dict[str, int | str]:
    count = equivalent_mapping_count(signs, anchors)
    return {
        "signs": signs,
        "externally_anchored_signs": anchors,
        "equivalent_bijective_mappings": str(count),
        "equivalent_mappings_scientific": f"{count:.6e}",
        "minimum_anchors_for_limit": minimum_anchors_for_limit(signs, limit),
        "mapping_limit": limit,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--signs", type=int, default=45)
    parser.add_argument("--anchors", type=int, default=0)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    answer = result(args.signs, args.anchors, args.limit)
    if args.json:
        print(json.dumps(answer, indent=2, sort_keys=True))
        return
    print(
        f"With {args.signs} signs and {args.anchors} external anchors, "
        f"there are {answer['equivalent_bijective_mappings']} "
        "structurally indistinguishable bijective relabelings."
    )
    print(
        f"At least {answer['minimum_anchors_for_limit']} fixed sign values are "
        f"needed to leave no more than {args.limit} relabelings."
    )


if __name__ == "__main__":
    main()
