.PHONY: help render preview publish clean check deps

help:
	@echo 'Targets:'
	@echo '  render   Render the full book (HTML + PDF) to _book/'
	@echo '  preview  Live preview in browser'
	@echo '  publish  Publish to Netlify (requires netlify-cli or token)'
	@echo '  clean    Remove rendered outputs and freeze cache'
	@echo '  check    Lint _quarto.yml and check chapter files exist'
	@echo '  deps     Install R package dependencies via pak'

render:
	quarto render

preview:
	quarto preview

publish:
	quarto publish netlify --no-prompt

clean:
	rm -rf _book _site _freeze .quarto

check:
	@test -f _quarto.yml || (echo 'missing _quarto.yml' && exit 1)
	@for f in index.qmd preface.qmd 00-intro.qmd references.qmd; do \
	  test -f $$f || (echo "missing $$f" && exit 1); \
	done
	@echo 'ok: top-level files present'
	@ls -1 [0-9][0-9]-*.qmd | grep -v '^00-' | wc -l | awk \
	  '{ if ($$1 == 18) print "ok: 18 chapter files"; \
	     else { print "error: expected 18 chapters, found " $$1; exit 1 } }'

deps:
	Rscript -e "if (!requireNamespace('pak', quietly = TRUE)) \
	  install.packages('pak'); \
	  pak::pak(c('rmarkdown', 'knitr', 'tidyverse', 'palmerpenguins'))"
