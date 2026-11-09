# Statistical Computing in the Age of AI
*2026-04-23 17:45 PDT*

Source repository for the open-access graduate textbook
**Statistical Computing in the Age of AI**.

- **Live site:** <https://rgtlab.org/scai>
- **License:** Creative Commons BY 4.0 (see `LICENSE.md`)
- **Format:** Quarto book (HTML + PDF)
- **Template:** Follows the conventions of the Posit/Hadley Wickham
  book family (e.g., `r4ds.hadley.nz`, `r-pkgs.org`).

## Local build

Prerequisites: Quarto 1.5+ and R 4.4+.

```bash
make deps       # install R package dependencies
make render     # render HTML + PDF to _book/
make preview    # live preview at http://localhost:4200
```

## Repository layout

```
.
├── _quarto.yml          book-level config
├── _variables.yml       reusable variables (course code, URL, etc.)
├── scai.scss            custom Bootstrap/SCSS theme
├── index.qmd            welcome page
├── preface.qmd          preface ('Why a new book?')
├── 00-intro.qmd         course-level introduction
├── 01-intro-r.qmd       Ch 1: Introduction to R (lecture 1)
├── ...                  (chapters 02 through 18)
├── 18-testing.qmd       Ch 18: package testing (lecture 19)
├── references.qmd       references page
├── references.bib       BibTeX bibliography
├── Makefile             render / preview / publish targets
└── netlify.toml         Netlify deploy config
```

## Chapter-to-lecture map

Each chapter stub includes a pointer to its source lecture directory
at `../lectures/lectureNN_DDmmmYY/`. Lecture 10 is Test 1 and has no
corresponding chapter.

| Chapter | Lecture | Topic                                    |
| ------- | ------- | ---------------------------------------- |
|  1      | 1       | Introduction to R                        |
|  2      | 2       | Version Control with Git                 |
|  3      | 3       | R Internals                              |
|  4      | 4       | Functional Programming                   |
|  5      | 5       | Matrix Algebra                           |
|  6      | 6       | Matrix Decompositions                    |
|  7      | 7       | Optimization and Numerical Methods       |
|  8      | 8       | Simulation Study Design                  |
|  9      | 9       | The Bootstrap                            |
| 10      | 11      | Linear Models                            |
| 11      | 12      | Generalized Linear Models                |
| 12      | 13      | Mixed-Effects Models                     |
| 13      | 14      | Visualization and the Grammar of Graphics|
| 14      | 15      | Advanced ggplot2                         |
| 15      | 16      | Interactive Visualization with Shiny     |
| 16      | 17      | Parallel Computing                       |
| 17      | 18      | R Package Development                    |
| 18      | 19      | Package Testing and Documentation        |

## Deploying to `rgtlab.org/scai`

Two options, in order of simplicity:

1. **Path-based proxy from the main rgtlab.org Netlify site.** Deploy
   this book to its own Netlify site (for example,
   `scai.netlify.app`), then add a redirect on the `rgtlab.org` site:

   ```
   /scai/*  https://scai.netlify.app/:splat  200
   ```

   This keeps the book deployment independent and is the recommended
   approach.

2. **Subdirectory build on the main rgtlab.org site.** Configure
   Netlify with `base = 'scai/'` and copy this repo into a
   corresponding directory of the main site repo. Harder to maintain.

## Contributing

This is a living text. Suggestions, corrections, and exercise
contributions are welcome via GitHub issues or pull requests.
