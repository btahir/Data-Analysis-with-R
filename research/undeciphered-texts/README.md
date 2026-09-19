# Undeciphered historical texts: an evidence-first research map

**Research snapshot:** 19 September 2026
**Scope:** historical scripts, codices, and information systems for which open
data could support a reproducible test—not a list of mysteries or claimed
translations.

## Executive conclusion

There is no responsible route from a frequency table or a language model to a
verified translation of the Voynich Manuscript. A decipherment is convincing
only when it predicts readings not used to construct it, explains spelling and
grammar consistently, fits the object's date and provenance, and is reproduced
by independent researchers. By those standards, the best projects are:

1. **Inka khipus** for structured-data reconstruction (but they are not a
   conventional written cipher);
2. **Linear A** for a versioned sign corpus and held-out structural tests;
3. **Proto-Elamite** for domain-constrained accounting hypotheses;
4. **Meroitic** for lexicon/grammar work—the signs can already be read; and
5. **Voynich** as an unusually good benchmark for *rejecting* weak methods.

The accompanying [candidate table](data/candidates.csv) makes the judgments
auditable, and [`prioritize.py`](scripts/prioritize.py) checks and regenerates
the [ranking](outputs/ranking.csv) using only the Python standard library. Scores
are research-triage judgments, not probabilities that a script will be solved.

Run it from the repository root:

```bash
python3 research/undeciphered-texts/scripts/prioritize.py
python3 -m unittest discover -s research/undeciphered-texts/tests -v
```

## First, separate four different problems

News coverage often calls all of these “codes,” although they require different
evidence:

| Problem | Example | What a solution must establish |
|---|---|---|
| Cryptographic ciphertext | a military radio message | key/system, plaintext, and operational context |
| Unknown script, possibly known language | Linear A | sign values plus language and grammar |
| Readable script, poorly understood language | Meroitic | vocabulary and grammar, not glyph substitution |
| Uncertain information system | khipu; perhaps rongorongo | whether and how the object encodes language |

This matters to the First World War analogy. Intercepted radio traffic normally
has many messages, dates, call signs, repeated formulae, and known military
context. Those are “cribs” and independent checks. A unique ancient artifact
usually has none. I could not confidently identify the particular recent WWI
story from the description alone; the project should not repeat that claim
without a title, archive reference, or link. The well-known **Silk Dress
cryptogram** was a nineteenth-century weather telegram, not a WWI radio code:
the NOAA reconstruction identifies the codebook, station reports, date, and
message purpose—exactly the kind of external validation ancient texts lack
([NOAA, 2024](https://www.noaa.gov/heritage/stories/code-breakers-unravel-130-year-old-mystery)).

## Candidate deep dives

### 1. Voynich Manuscript — rich data, almost no anchor

For the expanded data inventory, historical context, theory registry, and
breadth-first experimental program, see the dedicated
[Voynich Manuscript research dossier](voynich/README.md).

The Beinecke Library's **MS 408** record supplies provenance, a complete digital
facsimile, and a conservative early-fifteenth-century date. Yale's material
study found historic materials and no simple modern ink/pigment red flag; that
does not prove the writing encodes language. The manuscript has repeated word-
like forms and positional regularities, but one artifact cannot provide an
independent parallel text.

**Data path**

- Treat [Beinecke MS 408](https://collections.library.yale.edu/catalog/2002046)
  as the image authority and preserve image identifiers and folio order.
- Compare at least two diplomatic transcriptions rather than silently choosing
  one; the [Takahashi transcription mirror](https://www.voynich.nu/data/)
  documents EVA-era files, while René Zandbergen's site explains transcription
  alphabets and uncertainty
  ([transliteration overview](https://www.voynich.nu/transcr.html)).
- Link every token back to folio, line, glyph span, and annotator decision.
  Analyses that begin with a normalized plaintext-like string discard the most
  important uncertainty.

**Tests worth doing:** inter-transcriber disagreement; scribal-hand and section
held-outs; token-position effects; null models preserving line length and glyph
frequency; whether a proposed grammar predicts unseen pages.

**What would verify a solution:** one sign system and parsing procedure fixed in
advance; coherent readings across herbal, astronomical, balneological, and
recipe sections; identification of independently attested names or text; and
blind prediction on withheld folios. An anagram, a few plant names, or improved
language-model perplexity is not a decipherment.

### 2. Linear A — best conventional-script target

Linear A appears across many independently excavated objects. Some signs
resemble later Linear B, whose sound values provide a testable but not automatic
starting hypothesis. Administrative formats, find spots, numerals, and repeated
sequences give more external structure than Voynich.

**Data path:** use the open [SigLA database](https://sigla.phis.me/) for signs,
inscriptions, and object context; reconcile it against the standard *GORILA*
editions rather than treating database labels as ground truth. Version sign
variants and damaged readings. The University of Texas overview is a useful
orientation, not a corpus
([Scripts and Prehistory of the Aegean](https://sites.utexas.edu/scripts/linear-a/)).

**Path to progress:** reproduce sign-frequency and adjacency results; infer
document templates by site and vessel type; test Linear B-derived phonetic
values on held-out formulae; reject language hypotheses that require shifting
sound values or one-off exceptions. A bilingual inscription or a securely
identified long name would change the problem dramatically.

### 3. Proto-Elamite — accounting structure is an anchor

The script survives on many administrative tablets. Numerical systems and
tablet layout constrain what entries can mean even where language is unknown.
The [Cuneiform Digital Library Initiative](https://cdli.mpiwg-berlin.mpg.de/)
publishes catalog records, images, and transliterations; its Proto-Elamite
pages and identifiers should be the stable join keys. The [ORACC
documentation](http://oracc.museum.upenn.edu/doc/) is useful for interoperable
cuneiform data conventions, though coverage must be checked per corpus.

**Path to progress:** download a frozen tablet set; distinguish signs from
numerals and metrological marks; model entries within tablet/layout class; test
commodity or personnel hypotheses by whether totals and subtotals balance on
unseen tablets. This can yield verified administrative semantics without
pretending that every sign has a phonetic reading.

### 4. Indus script — important, but statistically underdetermined

The corpus has many objects but overwhelmingly short sequences, uncertain sign
variants, duplicates/impressions, and no accepted bilingual. Competing catalog
numbering and access restrictions make corpus provenance part of the research
problem. Harvard's [Indus script project](https://www.harappa.com/indus3/)
provides scholarly orientation, while the archaeological object records in the
[British Museum collection](https://www.britishmuseum.org/collection) and
excavation publications provide object-level checks.

**Path to progress:** publish a crosswalk among major concordances; separate
artifact, impression, photograph, and inscription; record reading direction
and damage as uncertainty; preregister tests that distinguish linguistic,
emblematic, and mixed systems. Sequence entropy or resemblance to one language
family is not enough. Short texts permit many mutually incompatible mappings.

### 5. Rongorongo — preservation precedes computation

Only a small number of inscribed wooden objects survive; provenance and copied
sign inventories are uneven, the corpus may be mnemonic rather than full
writing, and the language recordings postdate the collapse of the reading
tradition. Object histories should begin with holding institutions such as the
[Smithsonian's Mamari-related catalog searches](https://www.si.edu/search/collection-images?edan_q=rongorongo)
and verified museum records, then be reconciled with Barthel line designations.

**Path to progress:** multispectral/3-D imaging, conservation metadata, expert
segmentation with alternatives, and an open sign graph linked to exact surface
coordinates. Do not train on modern redrawings as though they were observations.
With so little material, a genuine advance is more likely to be a better reading
of the object than a full translation.

### 6. Cypro-Minoan — small but plural and contextualized

The corpus contains independently provenanced inscriptions on several media,
with possible sign relations to Aegean scripts. The data are much smaller and
less standardized than Linear A. Start from institutional records and the
[CREWS project](https://crewsproject.wordpress.com/) research bibliography,
then encode edition, object, sign variant, damage, find spot, and proposed
reading separately.

**Path to progress:** build an edition crosswalk and test whether proposed
subsystems truly differ after accounting for medium, site, and scholar-specific
sign splitting. Reserve complete inscriptions by site as out-of-sample tests.

### 7. Rohonc Codex — digitization and provenance first

This single illustrated manuscript has many symbols and competing cipher,
shorthand, invented-language, and hoax hypotheses. Benedek Láng's historical
study is a better starting point than viral “solutions”
([publisher record](https://www.psupress.org/books/titles/978-0-271-06779-9.html)).
The holding institution, the Hungarian Academy of Sciences, should be the
authority for images and codicology
([Library and Information Centre](https://konyvtar.mta.hu/index_en.php)).

**Path to progress:** obtain/licence a complete image set; create independent
double-keyed diplomatic transcriptions; map symbols to page coordinates; test
direction, spacing, abbreviation, and homophonic-cipher hypotheses. No lexical
claim is testable until the transcription and material chronology are open.

### 8. Phaistos Disc — a negative control for overclaiming

The disc has only 241 impressions made from 45 sign types on two sides. Even a
perfect transcription is too short and too isolated to select a unique language
and sign mapping. The Heraklion Archaeological Museum is the object authority
([museum portal](https://www.heraklionmuseum.gr/en/)). Use it to demonstrate how
many convincing-looking “translations” can be fitted to tiny data, not as the
lead solve target.

### 9. Khipu — strongest structured-data opportunity

Decimal knot values and accounting uses are established, while color, cord
attachment, hierarchy, and non-numerical signs may encode more. The [Open Khipu
Repository](https://github.com/khipufieldguide/Open-Khipu-Repository) makes
records and code inspectable, and the [Khipu Field Guide](https://khipufieldguide.com/)
documents the data model and objects. Museum records and original notes remain
necessary because legacy datasets contain interpretive fields.

**Path to progress:** validate calculated values from knot topology; model
missing cords explicitly; use linked colonial census/accounting documents only
as preregistered anchors; hold out complete khipus or archive groups. Predicting
known sums, hierarchy, and cross-document correspondences is a verifiable gain
even without prose “translation.”

### 10. Meroitic — not an undeciphered script

Meroitic signs have phonetic values; much vocabulary and grammar remain poorly
understood. The [Meroitic Newsletter digital archive](http://meroiticnewsletter.org/)
and museum corpora can support a versioned lexicon and context graph. Progress
should be judged by consistent morphology, loanwords/names with external
attestation, and predictions across unseen texts—not by claiming to crack the
alphabet again.

## Reproducible verification protocol

1. **Register the claim.** State whether it is segmentation, direction, sign
   value, word boundary, language identification, translation, or object date.
2. **Freeze the evidence.** Record checksums, edition/image IDs, licenses,
   exclusions, restorations, and all sign-merging rules.
3. **Represent uncertainty.** Keep alternative readings and damaged/illegible
   signs; never turn editorial guesses into observed characters.
4. **Define baselines.** Compare against shuffled, Markov, layout-preserving,
   and frequency-matched null corpora, not only modern natural languages.
5. **Prevent leakage.** Hold out entire objects, sites, hands, or sections—not
   random tokens from the same formula.
6. **Demand risky predictions.** A hypothesis must predict unseen sequences,
   totals, names, or morphology before inspection.
7. **Triangulate externally.** Require archaeology, material science,
   iconography, chronology, or an independently known text to agree.
8. **Invite adversarial replication.** Publish data transformations, code,
   negative results, and the exact conditions that would falsify the claim.

### Minimum acceptance ladder

| Level | Claim | Minimum evidence |
|---|---|---|
| 0 | visual pattern | reproducible measurement and uncertainty |
| 1 | structural regularity | beats structure-preserving nulls out of sample |
| 2 | semantic class | predicts external metadata/quantities |
| 3 | sign value or lexeme | recurs consistently and has an external anchor |
| 4 | grammatical reading | productive rules on unseen complete objects |
| 5 | decipherment | independent replication plus historical validation |

## A feasible first project (12 weeks)

Choose **Linear A**, not Voynich, for the first attempt.

- **Weeks 1–2:** snapshot SigLA metadata and document reuse/licensing; create a
  GORILA/SigLA identifier crosswalk.
- **Weeks 3–4:** double-review sign variants, damage, numerals, find spots, and
  object types; publish a data card.
- **Weeks 5–6:** reproduce basic frequencies and formulae with uncertainty
  sensitivity analyses.
- **Weeks 7–8:** establish shuffled, Markov, and document-template baselines.
- **Weeks 9–10:** preregister one narrow hypothesis (for example, whether a
  formula position predicts transaction role) and lock site-level holdouts.
- **Weeks 11–12:** evaluate, publish failures as well as successes, and request
  epigrapher review before making linguistic claims.

In parallel, use Voynich and the Phaistos Disc as stress tests: a method that
“translates” both with flexible post-hoc mappings has demonstrated overfitting,
not decipherment.

## Concrete open problems

Yes—there are tractable problems here, but most are **measurement and
verification problems before they are translation problems**. The complete,
machine-readable backlog is in [`data/open_problems.csv`](data/open_problems.csv).
It records the required data, proposed method, success and failure conditions,
principal risk, priority, status, and result for ten experiments. **PD-01 is now
solved in its narrow, preregistered scope:** the exact combinatorial analysis
proves that intrinsic label-invariant evidence leaves `45!` equally fitting
bijective relabelings. See the [full result and proof](results/phaistos-nonidentifiability.md).

The best first three are:

1. **Linear A cross-site prediction (LA-01).** Test whether positions in repeated
   formulae predict administrative roles when an entire archaeological site is
   withheld. This can falsify the claim that a pattern is grammatical rather
   than a local scribal template.
2. **Proto-Elamite ledger constraints (PE-01).** Ask whether a fixed assignment
   of signs to commodity/personnel classes predicts totals on unseen tablets.
   Arithmetic agreement supplies an external constraint without requiring a
   speculative full-language reading.
3. **Khipu archive relationships (KH-01).** Recalculate knot values from object
   structure and test whether color, attachment, and hierarchy predict sums or
   parent-child relationships in wholly held-out archive groups.

Three especially useful *foundation* problems are:

- **Voynich robustness (VM-01):** determine which famous word-position and
  repetition effects survive alternate transcriptions, segmentations, hands,
  and manuscript sections.
- **Indus corpus bias (IN-01):** quantify how duplicate seal impressions and
  competing sign catalogs change entropy and adjacency conclusions.
- **Rongorongo sign reality (RR-01):** test whether experts can recover proposed
  sign distinctions directly from calibrated object images rather than modern
  drawings.

One problem now has a bounded answer:

- **Phaistos non-identifiability (PD-01):** with 45 unanchored signs, there are
  exactly `45!` (about `1.196 × 10^56`) bijective labelings that preserve every
  equality-based structural observation. Even 35 external sign anchors leave
  `10! = 3,628,800` relabelings. This proves that internal repetition and
  frequency evidence cannot uniquely identify sign values.

These projects can produce valuable negative results. Failure on a stated
condition narrows the hypothesis space; it is not permission to change the
mapping after inspecting the holdout. Conversely, statistical regularity alone
does not establish phonetic values, language identity, or translation.

## Data notes and limitations

- Counts in `candidates.csv` are deliberately approximate because editions
  merge signs, objects, duplicates, fragments, and damaged readings differently.
- “Digital data” scores availability and machine-actionability together;
  “license clarity” must be rechecked before redistribution.
- The 0–3 rubric covers **data**, **external anchors**, **internal structure**,
  and **independent validation**. Equal weights are transparent defaults, not a
  scientific law.
- Museum portals change. A production dataset must store persistent object IDs,
  retrieval dates, checksums, and license snapshots.
- This survey prioritizes primary corpora and institutional records. Linked
  overview pages are discovery aids, not evidence for a decipherment.

## Source-quality rule

A proposed solution should cite the artifact/corpus edition, not merely a news
story. Peer review is useful but not sufficient; acceptance depends on open
readings and independent prediction. Conversely, “undeciphered” does not mean
mystical: often the honest limit is simply too little text, no bilingual, or no
known related language.
