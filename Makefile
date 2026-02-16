# -----------------------------------------------------------------------------
# FCAF Makefile
#
# Common usage:
#   make install_deps
#   make local_serve
#   make local_serve_versions
#   make ci_mike_deploy VERSION=0.0.1
#   make pdf VERSION=0.0.1
#   make dist VERSION=0.0.1
#   make clean
#
# Notes:
# - Creates a local Python venv in .venv (both locally and in CI).
# - PDF build uses Pandoc + XeLaTeX (Eisvogel template).
# - Mermaid blocks in PDFs are rendered via Mermaid CLI (mmdc) + Inkscape.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Paths / files
# -----------------------------------------------------------------------------
DOCS_DIR        := docs
OVERVIEW_DOC    := $(DOCS_DIR)/overview/index.md
FCAF_DIR        := $(DOCS_DIR)/fcaf
FCAF_DOCS       := $(shell find $(FCAF_DIR) -type f -name '*.md' | LC_ALL=C sort)

# PDF inputs (in order)
SOURCE_DOCS     := $(OVERVIEW_DOC) $(FCAF_DOCS)

BUILD_DIR       := build
SITE_DIR        := site

VERSION         ?= dev
BUILD           := $(shell date +%Y%m%d.%H%M%S)

REQ_FILE        := requirements.txt

# -----------------------------------------------------------------------------
# Python / venv
# -----------------------------------------------------------------------------
VENV_DIR ?= .venv
PYTHON   ?= $(VENV_DIR)/bin/python
PIP      ?= $(PYTHON) -m pip
MKDOCS   ?= $(VENV_DIR)/bin/mkdocs
MIKE     ?= $(VENV_DIR)/bin/mike

# -----------------------------------------------------------------------------
# PDF tooling
# -----------------------------------------------------------------------------
PANDOC          := pandoc
PDF_ENGINE      := xelatex

PANDOC_DATA_DIR := pandoc
PDF_TEMPLATE    := templates/eisvogel.latex
METADATA_FILE   := metadata.yml

PDF_OUT         := $(BUILD_DIR)/pdf/fcaf-framework.pdf

# -----------------------------------------------------------------------------
# Targets
# -----------------------------------------------------------------------------
.PHONY: help all venv install_deps mkdocs serve local_serve         local_serve_versions ci_mike_deploy pdf dist clean ci_clean

all: mkdocs

help:
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "  make install_deps                      Create venv + install requirements.txt"
	@echo "  make local_serve                       Run MkDocs locally (dev server)"
	@echo "  make local_serve_versions              Run mike serve locally (versioned)"
	@echo "  make mkdocs                            Build static HTML site"
	@echo "  make ci_mike_deploy VERSION=x.y.z      Deploy versioned site with mike (push)"
	@echo "  make pdf VERSION=x.y.z                 Build PDF from overview + all docs/fcaf/**/*.md"
	@echo "  make dist VERSION=x.y.z                Zip PDFs into build/dist/"
	@echo "  make clean                             Remove build artifacts + venv"
	@echo ""

# -----------------------------------------------------------------------------
# Python env / deps
# -----------------------------------------------------------------------------
venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	@$(PIP) install --upgrade pip setuptools wheel

install_deps: venv
	@test -f $(REQ_FILE) || (echo "$(REQ_FILE) not found"; exit 1)
	@$(PIP) install -r $(REQ_FILE)
	@echo "Installed Python dependencies from $(REQ_FILE)."

# -----------------------------------------------------------------------------
# MkDocs
# -----------------------------------------------------------------------------
mkdocs: install_deps
	$(MKDOCS) build

serve: install_deps
	$(MKDOCS) serve

local_serve: serve

# -----------------------------------------------------------------------------
# Versioned site (mike)
# -----------------------------------------------------------------------------
local_serve_versions: install_deps
	$(MIKE) serve

# CI: deploy versioned site to gh-pages
ci_mike_deploy: install_deps
	@if [ -z "$(VERSION)" ]; then \
	  echo "VERSION not set. Usage: make ci_mike_deploy VERSION=0.0.1"; \
	  exit 1; \
	fi
	@PATH="$(CURDIR)/.venv/bin:$$PATH" \
	  $(MIKE) deploy --push --update-aliases "$(VERSION)" latest
	@PATH="$(CURDIR)/.venv/bin:$$PATH" \
	  $(MIKE) set-default --allow-empty --push latest

# -----------------------------------------------------------------------------
# PDF generation
# -----------------------------------------------------------------------------
pdf:
	@command -v $(PANDOC) >/dev/null || (echo "pandoc not installed"; exit 1)
	@mkdir -p $(BUILD_DIR)/pdf
	$(PANDOC) \
		--from markdown+gfm_auto_identifiers \
		--toc \
		--pdf-engine=$(PDF_ENGINE) \
		--data-dir=$(PANDOC_DATA_DIR) \
		--template=$(PDF_TEMPLATE) \
		--resource-path=$(DOCS_DIR):$(DOCS_DIR)/media:build \
		--lua-filter=$(PANDOC_DATA_DIR)/filters/mermaid.lua \
		--metadata date="v$(VERSION)  $(BUILD)" \
		$(PANDOC_DATA_DIR)/$(METADATA_FILE) \
		-o $(PDF_OUT) \
		$(SOURCE_DOCS)

dist:
	@mkdir -p $(BUILD_DIR)/dist
	@ls -1 $(BUILD_DIR)/pdf/*.pdf >/dev/null 2>&1 || (echo "No PDFs found in $(BUILD_DIR)/pdf. Run 'make pdf' first."; exit 1)
	zip -j "$(BUILD_DIR)/dist/fcaf-pdfs-v$(VERSION).zip" $(BUILD_DIR)/pdf/*.pdf

# CI-friendly clean (keeps venv to speed up re-runs)
ci_clean:
	rm -rf $(BUILD_DIR) $(SITE_DIR)

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------
clean:
	rm -rf $(BUILD_DIR) $(SITE_DIR) $(VENV_DIR)
