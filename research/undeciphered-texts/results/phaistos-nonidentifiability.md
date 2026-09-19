# PD-01 result: the Phaistos Disc is intrinsically label-non-identifiable

**Status:** solved for bijective sign relabeling under intrinsic,
label-invariant evidence. This is a proof of a limitation, not a decipherment.

## Question

How many incompatible sign-to-label mappings fit the complete inscription
equally well when the evidence is limited to its internal structure?

## Result

The disc uses 45 sign types. With no externally fixed sign values, there are

```text
45! = 119622220865480194561963161495657715064383733760000000000
    ≈ 1.196222 × 10^56
```

bijective relabelings that preserve every position, repeated-sign relation,
frequency multiset, repetition distance, and equality-pattern n-gram. Even if
35 sign values were externally fixed, the remaining ten signs admit
`10! = 3,628,800` relabelings. At least 36 of the 45 signs must be fixed to
bring this particular equivalence class below one million (`9! = 362,880`).

## Proof

Let the observed sign alphabet be a set **S** of size *n*. Let **L** be any set
of *n* proposed distinct labels. A bijection `f: S → L` can be selected in `n!`
ways. For every pair of positions *i* and *j*, `S[i] = S[j]` if and only if
`f(S[i]) = f(S[j])`, because *f* is one-to-one. Therefore every statistic that
depends only on positions and sign equality is unchanged by *f*. Fixing *k*
externally verified pairs leaves a free permutation of the other `n-k` labels,
so the equivalence class has exactly `(n-k)!` members. ∎

This conclusion does not require choosing a disputed reading direction or word
segmentation: bijective relabeling preserves either choice.

## Reproduction

From the repository root:

```bash
python3 research/undeciphered-texts/scripts/phaistos_nonidentifiability.py
python3 research/undeciphered-texts/scripts/phaistos_nonidentifiability.py --json
```

The calculation uses exact integer factorials from the Python standard library.

## What this solves—and what it does not

This resolves PD-01's narrow identifiability question for substitution-like
readings judged only by intrinsic, label-invariant structure: there is a vast,
exact equivalence class, so that evidence cannot select a unique mapping.

It does **not** say all natural-language readings receive equal probability
under a specified external language model. Such a model adds assumptions about
language, phonotactics, sign function, and segmentation. Those assumptions may
rank mappings, but the ranking is no longer evidence supplied by the disc alone.
Likewise, allowing homophony, polyphony, logograms, nulls, or variable
segmentation expands the hypothesis class beyond the bijective case measured
here.

Accordingly, a claimed decipherment must introduce external constraints: a
parallel text, independently known names, securely related inscriptions, or a
fixed language model selected before inspecting candidate readings. Fit to the
disc's repetitions and frequencies cannot, by itself, identify sign values.
