# Voynich Manuscript research dossier

**Object:** Beinecke Rare Book and Manuscript Library, MS 408  
**Research question:** which properties of the writing survive uncertainty in
the images, transcription, tokenization, scribal hand, and manuscript section?

This dossier is a starting point for reproducible research, not a claimed
translation. The first objective is to construct evidence capable of rejecting
bad explanations. A reading will count as a decipherment only if a fixed method
predicts unseen material and is independently replicated.

## Why the Voynich Manuscript is so hard to decipher (briefly)

The manuscript is difficult because it is one illustrated book with no known
parallel text, no agreed language, no confirmed proper names, and no external
key. Researchers also disagree about some glyph boundaries, rare characters,
word boundaries, and which marks are meaningful. Its illustrations suggest
broad subject areas but usually do not identify a plant, star, recipe, or label
unambiguously. Consequently, many incompatible systems can be adjusted to fit
the same short strings. Internal statistical regularity can show that the marks
are structured; it cannot by itself tell us what they mean.

## 1. What is securely known

### The physical object

- Yale catalogues the manuscript as **MS 408** and provides the authoritative
  digital facsimile and folio sequence.
- The support is parchment. Radiocarbon measurements reported by the University
  of Arizona place sampled parchment in the early fifteenth century, commonly
  summarized as 1404–1438 CE. This dates the animal skin, not necessarily the
  precise day on which every mark was made.
- Yale's materials work found inks, pigments, and construction consistent with
  a historical manuscript. That makes a modern Wilfrid Voynich fabrication
  unlikely, but does not establish that the text encodes language.
- The book has missing leaves and foldouts. Modern foliation, historical quire
  order, and the order in which pages were written are not identical questions.
- Its commonly named visual sections are herbal, astronomical/astrological,
  biological or balneological, cosmological, pharmaceutical, and recipes. These
  labels are modern descriptions, not decoded headings.

### Provenance

The secure modern chain runs through bookseller Wilfrid Voynich, the Jesuit
collection at Villa Mondragone, and Yale. Earlier ownership is reconstructed
from a seventeenth-century letter associated with Johannes Marcus Marci and
Athanasius Kircher, plus partially erased ownership evidence often associated
with Jacobus de Tepenec. Rudolf II is reported in that chain, but the report is
not equivalent to a surviving imperial inventory entry. Provenance claims must
therefore be tagged as physical, documentary, reported, or speculative.

### Observable textual structure

Without assuming a language, researchers can safely say that:

- glyph-like units form space-delimited groups conventionally called “words”;
- distributions vary by location within lines, paragraphs, folios, sections,
  and the clusters conventionally called Currier A and Currier B;
- similar word forms recur with small changes, and some forms favor particular
  positions;
- labels and short strings near illustrations behave differently from running
  text; and
- more than one scribal hand is a serious palaeographic hypothesis.

These are constraints for a model. They are not translations.

## 2. Data inventory

The machine-readable [source manifest](data/sources.csv) records the datasets we
should acquire, their role, and important cautions.

### Images and physical evidence

1. **Beinecke MS 408 images and catalog record** are the image authority. Store
   Yale's identifiers, folio labels, dimensions, and retrieval date rather than
   renaming images without a crosswalk.
2. **Multispectral and materials evidence** should be used only when Yale or the
   holding institution releases the underlying data or documented results.
   Enhanced images must never silently replace ordinary-light images.
3. Each observation needs coordinates on an image, not merely a line number in
   somebody else's transcription.

### Transcriptions

The EVA alphabet is an interchange convention, not a claim about phonetic
values. The commonly used interlinear corpus aggregates readings by multiple
transcribers; Takahashi's transcription is useful and influential, but is not
an independent view of the physical object for every analytical purpose.

We should preserve:

- original glyph strings and uncertainty codes;
- folio, side, line, and locus identifiers;
- transcriber identity and transcription version;
- spaces, paragraph marks, line breaks, labels, and uncertain gaps; and
- alternative parses where a stroke may be one glyph, part of a compound, or
  scribal ornament.

Never convert uncertain characters to a convenient single symbol before the
sensitivity analysis.

### Metadata

Useful metadata include folio/quire, illustration section, paragraph and line
position, Currier language, proposed scribal hand, ink or writing phase when
supported, label versus running text, and damage. Every category needs a source
and confidence field; disputed scholarly labels are not ground truth.

## 3. Search space: major explanation families

The [hypothesis registry](data/hypotheses.csv) converts broad theories into
predictions and failure conditions. The main families are:

1. **Natural language in an unusual script.** Candidates have included Latin,
   Romance, Germanic, Slavic, Greek, Semitic, Turkic, and other languages.
   A serious proposal must specify morphology, syntax, sound/sign assignments,
   and how these generalize—not just match a few illustrated words.
2. **Cipher over a natural language.** Simple substitution is a poor fit to the
   full set of positional and word-formation effects unless additional rules
   are introduced. Homophones, nulls, nomenclators, verbose cipher units, and
   transposition greatly enlarge the search space, so complexity penalties and
   held-out predictions are essential.
3. **Abbreviation, shorthand, or technical notation.** Medieval medical,
   alchemical, astrological, and scribal abbreviation practices are relevant
   comparanda, but a resemblance between one glyph and one abbreviation is not
   enough. The system must explain complete lines consistently.
4. **Constructed or encoded language.** This can explain unusual statistics but
   is flexible enough to become unfalsifiable unless its generation rules are
   fixed before evaluation.
5. **Algorithmic pseudo-text or hoax.** Repetition with small local alterations
   can be generated without semantic content. Such models must reproduce the
   manuscript's section, hand, line, and paragraph effects and must beat simpler
   structured-language baselines.
6. **Mixed system.** Labels, tables, recipes, and prose might use different
   conventions. This is plausible but increases model freedom; the partition
   must be motivated independently, not chosen to rescue a failed reading.

No family currently has the external anchors required for a verified solution.

## 4. Historical context that can constrain—not determine—the answer

The parchment date places production in a Europe where Latin was the dominant
scholarly language, while Italian, German, French, Czech and other vernaculars
were widely written. Greek and Hebrew scholarship, Arabic scientific texts in
translation, multilingual trade, and mobile medical and religious communities
all matter. Plausible cultural contexts include university medicine, household
recipe books, herbals, bathing regimens, astrology, alchemy, and apothecary
practice.

This creates a comparison set, not a license to choose whichever language makes
a word resemble a desired plant name. For each candidate context we should build
dated control corpora (approximately 1350–1450, widened only in preregistered
sensitivity checks) with known region, genre, and scribal conventions:

- Latin, Italian, German, French, and Czech herbals and recipe collections;
- astronomical and astrological tables and calendars;
- medical bathing, women's-health, pharmacological, and alchemical manuscripts;
- contemporary cipher manuals, nomenclators, shorthand, and abbreviation lists;
- Greek, Hebrew, and translated Arabic scientific material demonstrably present
  in the relevant European networks; and
- nonlinguistic controls generated by copying, tables, or constrained stochastic
  processes.

Comparisons must be genre- and layout-matched. A modern newspaper corpus is not
a meaningful baseline for a fifteenth-century recipe manuscript.

## 5. Breadth-first research program

“Breadth first” should mean eliminating whole explanation families with common,
predeclared tests before optimizing any favorite language.

### Phase 0 — freeze evidence and provenance

1. Record hashes, licenses, versions, URLs, and retrieval dates for every file.
2. Build a canonical folio/line/image-coordinate crosswalk.
3. Keep raw inputs immutable; transformations produce new versioned artifacts.
4. Document excluded pages, unreadable spans, and editorial interventions.

**Exit condition:** another researcher can recreate the same analysis table from
the same source versions.

### Phase 1 — measure transcription uncertainty

Align at least two transcriptions to image coordinates. Calculate agreement for
glyph identity, glyph boundaries, spaces, line breaks, and rare signs. Represent
disagreement as an alignment graph rather than selecting a winner.

**Decisive result:** identify which published “regularities” change sign or
vanish under defensible alternate readings. This directly addresses VM-01.

### Phase 2 — establish null models

Use a ladder rather than one straw-man control:

- shuffled glyphs preserving unigram counts;
- shuffled words preserving line length;
- Markov models preserving local transitions;
- copy-and-mutate generators;
- layout-aware models preserving paragraph and line position; and
- matched historical-language corpora passed through plausible abbreviation or
  cipher channels.

Evaluate held-out likelihood, calibration, compression, and the specific
statistics the model was *not* tuned to reproduce.

### Phase 3 — map variation before language identification

Quantify section, quire, folio, scribal-hand, paragraph, line, and illustration
effects with hierarchical models. Hold out whole folios and hands. This tests
whether Currier A/B behavior is linguistic, scribal, topical, chronological, or
a mixture without assuming that any cluster is a language.

### Phase 4 — morphology and syntax candidates

Build tokenization lattices and test whether reusable prefix/stem/suffix analyses
predict unseen forms. Compare against copy-and-mutate and positional templates.
Require a compact grammar with explicit exception counts. Do not translate yet.

### Phase 5 — historical-language and cipher screens

For each historically motivated language/cipher pair:

1. specify the sign inventory, segmentation, transformation rules, lexicon, and
   permitted abbreviations in advance;
2. train or choose hyperparameters without the final held-out folios;
3. score full lines, not selected words;
4. penalize nulls, homophones, anagrams, optional substitutions, and exceptions;
5. compare with rival languages and pseudo-text generators under the same
   parameter budget; and
6. publish failures as well as the best score.

### Phase 6 — semantic anchoring

Only after a structural model survives should we test illustration-linked
labels. Candidate identifications must come from independent art-historical or
botanical assessment, with multiple possible identifications retained. The model
must predict withheld labels and prose, not learn its dictionary from them.

### Phase 7 — adversarial replication

Freeze code, mappings, and held-out pages. Give images—not expected readings—to
an independent team. A viable decipherment must produce consistent grammar and
meaning across sections, recover independent historical anchors, and make novel
predictions that can fail.

## 6. Analyses to run first

1. **Transcription robustness matrix:** rerun word frequency, conditional
   entropy, line-position, and repetition statistics across every transcription
   and uncertainty sample.
2. **Artifact-level held-outs:** hold out complete folios, quires, sections, and
   scribal hands rather than random tokens, which leak near-duplicates.
3. **Copy-distance analysis:** measure whether near-neighbor variants depend on
   physical distance on the page after controlling for frequency and position.
4. **Boundary sensitivity:** repeat every word-level result over plausible space
   deletion/insertion and compound-glyph parses.
5. **Writer-versus-topic model:** compare hierarchical models for hand, section,
   and their interaction; test on hands and folios excluded from fitting.
6. **Description-length tournament:** compare natural-language channels,
   cipher/abbreviation systems, and pseudo-text generators including the bits
   required to state exceptions and dictionaries.

These analyses can narrow the field. None alone supplies semantics.

## 7. What would count as solving it

A credible solution must provide all of the following:

- a stable image-to-glyph transcription procedure;
- fixed reading direction, segmentation, sign values, and transformation rules;
- a language identification supported by ordinary grammar across full passages;
- low exception and free-parameter counts relative to competitors;
- consistent readings across sections, hands, and unseen folios;
- at least one external anchor not selected after seeing the proposed reading;
- predictions registered before opening the final test material; and
- independent reproduction from the manuscript images.

Finding several plausible words, assigning plants after seeing illustrations,
or obtaining better perplexity than modern English is not sufficient.

## 8. Immediate next step

Acquire and checksum the sources in `data/sources.csv`, verify their reuse terms,
and create the coordinate-preserving multi-transcription corpus. We should not
claim to “try every language” before this foundation exists: doing so would
multiply researcher degrees of freedom and virtually guarantee false matches.

## Sources and orientation

- [Beinecke Library catalog record and facsimile, MS 408](https://collections.library.yale.edu/catalog/2002046)
- [Beinecke overview of the Voynich Manuscript](https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript)
- [University of Arizona report on parchment dating](https://news.arizona.edu/news/ua-experts-determine-age-book-nobody-can-read)
- [Yale scientific analysis overview](https://news.yale.edu/2009/12/04/analysis-voynich-manuscript)
- [René Zandbergen, transcription systems and corpus history](https://www.voynich.nu/transcr.html)
- [Voynich.nu transcription data index](https://www.voynich.nu/data/)
- [Reddy and Knight, *What We Know About the Voynich Manuscript* (ACL 2011)](https://aclanthology.org/W11-1511/)
- [Montemurro and Zanette, keyword and long-range structure study](https://doi.org/10.1371/journal.pone.0066344)
- [Davis, palaeographic study of scribal hands](https://muse.jhu.edu/article/754633)

Secondary orientation sites are useful for locating claims, but all decisive
metadata and measurements should be traced to the holding institution, the
physical object, or a citable research publication.
