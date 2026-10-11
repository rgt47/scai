# Merging scai-advanced into scai
*2026-10-11 10:57 PDT*

Configuration for one HTML book and two print volumes. The profile
files below live in `analysis/report/`.

**Status (2026-10-11, step 1 done).** Files renamed and copied, 04's
working-tree copy of `11b-reproducible-environments.qmd` used (it
carried an uncommitted wording fix), bibliographies merged (144
entries; 8 shared keys differed only in formatting, 03's version
kept), `sec-intro` collision fixed, 04's notation section added to
`conventions.qmd`. HTML renders with no unresolved cross-references.

**Status (2026-10-11, step 2 done).** Text edits 1 to 3 below are
complete; preface, index, and introduction describe one book in two
halves; 04's credits and acknowledgments folded in; the Volume II
cover regenerated with the merged title. Remaining: redirects and
deploy, the cross-volume filter, then content harmonization.

## Files

| File | Role |
|---|---|
| `_quarto.yml` | Shared settings; `profile: default: html` |
| `_quarto-html.yml` | Full book, chapters 1 to 33, `_book/` |
| `_quarto-vol1.yml` | Volume I PDF, chapters 1 to 15, `_book-vol1/` |
| `_quarto-vol2.yml` | Volume II PDF, chapters 16 to 33, `_book-vol2/` |

## Balance

| Volume | Chapters | Words (current text) |
|---|---|---|
| I, first quarter | 15 | about 63,000 |
| II, second quarter | 18 | about 60,000 |

Moved from the old first quarter to the second: `bayesian`,
`parallel`, `packages`, `testing`, `shiny`. Each now sits next to the
04 chapter it overlaps. Consolidating those pairs later shrinks
Volume II, and the boundary should then be revisited.

## File renames

Chapter files drop their numeric prefixes, since Quarto numbers
chapters by position. Old HTML URLs need Netlify redirects.

| New name | From 03 | From 04 |
|---|---|---|
| `intro.qmd` | `00-intro.qmd` | |
| `intro-r.qmd` | `01-intro-r.qmd` | |
| `git.qmd` | `02-git.qmd` | |
| `r-internals.qmd` | `03-r-internals.qmd` | |
| `functional.qmd` | `04-functional.qmd` | |
| `matrix-algebra.qmd` | `05-matrix-algebra.qmd` | |
| `decompositions.qmd` | `06-decompositions.qmd` | |
| `optimization.qmd` | `07-optimization.qmd` | |
| `simulation.qmd` | `08-simulation.qmd` | |
| `bootstrap.qmd` | `09-bootstrap.qmd` | |
| `linear-models.qmd` | `10-linear-models.qmd` | |
| `glm.qmd` | `11-glm.qmd` | |
| `mixed-models.qmd` | `12-mixed-models.qmd` | |
| `survival.qmd` | `13-survival.qmd` | |
| `bayesian.qmd` | `14-bayesian.qmd` | |
| `viz-grammar.qmd` | `15-viz-grammar.qmd` | |
| `ggplot2-advanced.qmd` | `16-ggplot2-advanced.qmd` | |
| `shiny.qmd` | `17-shiny.qmd` | |
| `parallel.qmd` | `18-parallel.qmd` | |
| `packages.qmd` | `19-packages.qmd` | |
| `testing.qmd` | `20-testing.qmd` | |
| `intro-advanced.qmd` | | `00-intro.qmd` |
| `numerical-stability.qmd` | | `01-numerical-stability.qmd` |
| `numerical-linalg.qmd` | | `02-numerical-linalg.qmd` |
| `advanced-optimization.qmd` | | `03-advanced-optimization.qmd` |
| `em-extensions.qmd` | | `04-em-extensions.qmd` |
| `monte-carlo.qmd` | | `05-monte-carlo.qmd` |
| `mcmc-depth.qmd` | | `06-mcmc-depth.qmd` |
| `modern-bayesian.qmd` | | `07-modern-bayesian.qmd` |
| `hpc.qmd` | | `08-hpc.qmd` |
| `high-dim.qmd` | | `09-high-dim.qmd` |
| `machine-learning.qmd` | | `10-machine-learning.qmd` |
| `software-engineering.qmd` | | `11-software-engineering.qmd` |
| `reproducible-environments.qmd` | | `11b-reproducible-environments.qmd` |
| `interactive-viz.qmd` | | `12-interactive-viz.qmd` |

Front matter (`half-title`, `copyright`, `index`, `preface`,
`conventions`, `credits`, `colophon`) comes from 03; merge in the 04
versions' content, especially `conventions.qmd`, which is longer in
04. Copy 04's `images/cover.png` to `images/cover-vol2.png`, and merge
the two `references.bib` files, removing duplicate keys.

## Edits required in chapter text

1. `intro-advanced.qmd`: change `{#sec-intro}` to
   `{#sec-intro-advanced .unnumbered}`. As written it is numbered and
   its label collides with 03's `sec-intro`. Rewrite 'The introductory
   volume, [link]' and the 'Chapters 1 and 2 ... 8 through 13' passage
   to the new numbering or to `@sec-` references.
2. Prose references to 'the introductory volume' become
   cross-references: `03-advanced-optimization.qmd:33`,
   `05-monte-carlo.qmd:28,307,494`, `04-em-extensions.qmd:37`,
   `02-numerical-linalg.qmd:31`, `06-mcmc-depth.qmd:32`.
3. Practice-test and quiz-answer labels (`sec-practice-test-NN`,
   `sec-quiz-answers-NN`) encode old 03 chapter numbers; rename them
   to chapter slugs (for example `sec-quiz-answers-bayesian`).

## Cross-volume references

In HTML every reference resolves. In the Volume II PDF, references to
Volume I chapters do not: the stub render printed `?@sec-simulation`
and Quarto warned 'Unable to resolve crossref'. Known cases from the
current text: `@sec-simulation` (twice), `@sec-mixed-models`,
`@sec-matrix-algebra`, plus `credits.qmd` (`@sec-mixed-models`),
which is printed in both volumes. In the reverse direction,
`preface.qmd:131` cites `@sec-bayesian`, which now sits in Volume II.
A small Lua filter that maps those labels to
'Volume I, Chapter N' is still needed before the volumes print.

The five references in 04 to 03 labels (the three chapter files
above plus `@sec-bayesian` in `06-mcmc-depth.qmd:32`) cannot resolve
in the standalone scai-advanced build today, since those labels exist
only in 03. The merge fixes them in HTML. (Inferred from the labels;
the live site was not checked.)

## Verification

A stub book (one heading and label per file, same names, same
configs) rendered in the scratchpad with Quarto 1.10.18:

- `--profile html`: 43 files; chapter titles read 15 for
  `ggplot2-advanced`, 16 for `numerical-stability`, 21 for
  `bayesian`, 33 for `interactive-viz`.
- `--profile vol2 --to pdf`: table of contents shows Parts VI to X
  and chapters 16 to 33, so the counter offsets work.
- `--profile vol1 --to pdf`: Parts I onward, chapters from 1.

Not verified: rendering of the real chapter text, page counts, the
cover images, and the US-spelling pre-render hook (stripped from the
stub).
