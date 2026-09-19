# Data-Analysis-with-R
Analyzing Red Wine Quality

## Undeciphered historical texts research

This repository now includes an
[evidence-first investigation of undeciphered historical texts](research/undeciphered-texts/README.md).
The project compares ten candidates—including the Voynich Manuscript, Linear A,
Proto-Elamite, the Indus script, rongorongo, the Phaistos Disc, and khipus—and
turns broad decipherment questions into testable research problems.

### What we completed

- Created a machine-readable [candidate dataset](research/undeciphered-texts/data/candidates.csv)
  and [open-problems dataset](research/undeciphered-texts/data/open_problems.csv).
- Defined an evidence and verification protocol based on frozen hypotheses,
  held-out artifacts, external anchors, risky predictions, and independent
  replication.
- Added a dependency-free [Python prioritizer](research/undeciphered-texts/scripts/prioritize.py)
  that validates candidate scores and reproducibly generates the
  [candidate ranking](research/undeciphered-texts/outputs/ranking.csv).
- Resolved the narrow Phaistos Disc problem **PD-01** by proving that its
  intrinsic, label-invariant structure cannot uniquely determine sign values.
  With 45 unanchored signs, `45!` bijective relabelings preserve the observed
  equality patterns; this is a limitation result, **not** a decipherment. See
  the [proof and its scope](research/undeciphered-texts/results/phaistos-nonidentifiability.md).
- Added unit tests for candidate validation, ranking, exact permutation counts,
  anchor thresholds, and invalid inputs.

The current recommendation is to pursue khipu structured-data analysis, Linear
A cross-site prediction, Proto-Elamite ledger reconstruction, and Meroitic
linguistic work. The Voynich Manuscript is most useful initially as a benchmark
for rejecting overfit methods.

### Where this work lives

The undeciphered-texts project **is part of this `Data-Analysis-with-R`
repository**; it is not stored in a separate repository. Its source data,
analysis scripts, tests, generated ranking, and written results are all under
[`research/undeciphered-texts/`](research/undeciphered-texts/README.md).

The analysis scripts use Python's standard library because the current tasks
are deterministic CSV validation, ranking, and combinatorics rather than an R
statistical workflow. The repository name does not require every analysis to be
implemented in R. The existing red-wine R Markdown project remains unchanged.

To reproduce the new analysis from the repository root, run:

```bash
python3 research/undeciphered-texts/scripts/prioritize.py
python3 research/undeciphered-texts/scripts/phaistos_nonidentifiability.py
python3 research/undeciphered-texts/scripts/phaistos_nonidentifiability.py --json
python3 -m unittest discover -s research/undeciphered-texts/tests -v
```

The complete methodology, source notes, candidate assessments, limitations, and
next-step research plan are in the
[project README](research/undeciphered-texts/README.md).

An expanded [Voynich Manuscript dossier](research/undeciphered-texts/voynich/README.md)
maps the available images and transcriptions, historical-language context,
competing theory families, falsification tests, and a staged breadth-first
research program.
