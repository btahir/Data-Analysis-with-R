# Data-Analysis-with-R
Analyzing Red Wine Quality

## Additional research

- [Undeciphered historical texts: evidence, datasets, and a reproducible path
  to testing proposed solutions](research/undeciphered-texts/README.md)

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
python3 -m unittest discover -s research/undeciphered-texts/tests -v
```
