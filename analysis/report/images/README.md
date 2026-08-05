# Images
*2026-04-23 19:06 PDT*

Image assets for **Statistical Computing in the Age of AI**.

## Policy

- **Cover image:** required. One image, placed here as `cover.png`
  (or `.jpg`/`.svg`). Referenced from `_quarto.yml` via
  `cover-image:` under the `book:` key. Should be clean and
  scholarly; either a hex-sticker composite (matches Posit book
  family convention) or a thematic still photograph.
- **Content figures only inside chapters.** Follow the Posit
  editorial discipline. Figures exist to teach. Do not add
  decorative chapter-opener images, AI-generated hero images, or
  part-divider art.
- **Portraits of foundational figures:** permitted sparingly (four
  to five across the book), placed in `portraits/`. Each portrait
  appears once, at the first substantive introduction of the
  figure, using a compact right-aligned block:

  ```markdown
  ![Bradley Efron, whose 1979 paper introduced the
   bootstrap.](images/portraits/efron.jpg){fig-align='right'
   width='25%'}
  ```

  All portraits must be CC-BY/CC0 or appear under permission;
  attribution goes in `credits.qmd`.

## Planned portraits

| Chapter                              | Figure                   | Reason                               |
| ------------------------------------ | ------------------------ | ------------------------------------ |
| Ch 6 Matrix Decompositions           | Gene H. Golub            | co-author, *Matrix Computations*     |
| Ch 7 Optimization                    | Jorge Nocedal            | co-author, *Numerical Optimization*  |
| Ch 9 The Bootstrap                   | Bradley Efron            | 1979 founding paper                  |
| Ch 11 Generalized Linear Models      | John A. Nelder           | GLM framework; Nelder-Wedderburn     |
| Ch 12 Mixed-Effects Models           | Douglas Bates            | `lme4` principal author              |

## Contributing an image

1. Obtain the image from a CC-BY/CC0 source (Wikimedia Commons,
   ICM video, Posit community), or from the subject's own public
   profile with permission.
2. Resize to approximately 400 px on the long edge; compress.
3. Save as `portraits/<surname>.jpg`.
4. Add an entry to `credits.qmd` with source URL, license, and
   attribution text.
5. Reference from the target chapter with the compact markdown
   block above.
