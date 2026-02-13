# -----------------------------------------------------------------------------
# FCAF Makefile
#
# Usage:
#   make help
#   make install_deps
#   make local_serve
#   make local_serve_versions
#   make mkdocs
#   make ci_mike_deploy VERSION=0.0.1
#   make pdf VERSION=0.0.1
#   make dist VERSION=0.0.1
#   make clean
#
# Notes:
# - Uses a local Python venv in .venv by default.
# - Designed to work both locally and in GitHub Actions.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Paths / files
# -----------------------------------------------------------------------------

DOCS_DIR        := docs
FCAF_DIR        := docs/fcaf

MAIN_DOC        := $(DOCS_DIR)/index.md
FCAF_DOCS       := $(wildcard $(FCAF_DIR)/*.md)
SOURCE_DOCS     := $(MAIN_DOC) $(FCAF_DOCS)

BUILD_DIR       := build
SITE_DIR        := site

VERSION         ?= dev
BUILD           := $(shell date +%Y%m%d.%H%M%S)

REQ_FILE        := requirements.txt

# -----------------------------------------------------------------------------
# Python / venv
# -----------------------------------------------------------------------------

VENV_DIR        := .venv
PYTHON          := $(VENV_DIR)/bin/python
PIP             := $(VENV_DIR)/bin/pip

MKDOCS          := $(VENV_DIR)/bin/mkdocs
MIKE            := $(VENV_DIR)/bin/mike

# -----------------------------------------------------------------------------
# PDF tooling (optional; CI installs via apt)
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

.PHONY: help all venv install_deps mkdocs serve local_serve \
        local_serve_versions ci_mike_deploy pdf dist clean

all: mkdocs

help:
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "  make help                              Show this help"
	@echo "  make install_deps                      Create venv + install requirements.txt"
	@echo "  make local_serve                       Run MkDocs locally (dev server)"
	@echo "  make local_serve_versions              Run mike serve locally (versioned)"
	@echo "  make mkdocs                            Build static HTML site"
	@echo "  make ci_mike_deploy VERSION=x.y.z      Deploy versioned site with mike (push)"
	@echo "  make pdf VERSION=x.y.z                 Build combined PDF (Pandoc + Eisvogel)"
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
	$(MIKE) deploy --push --update-aliases "$(VERSION)" latest
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
		--metadata date="v$(VERSION)  $(BUILD)" \
		$(PANDOC_DATA_DIR)/$(METADATA_FILE) \
		-o $(PDF_OUT) \
		$(SOURCE_DOCS)

dist:
	@mkdir -p $(BUILD_DIR)/dist
	@ls -1 $(BUILD_DIR)/pdf/*.pdf >/dev/null 2>&1 || (echo "No PDFs found in $(BUILD_DIR)/pdf. Run 'make pdf' first."; exit 1)
	zip -j "$(BUILD_DIR)/dist/fcaf-pdfs-v$(VERSION).zip" $(BUILD_DIR)/pdf/*.pdf

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

clean:
	rm -rf $(BUILD_DIR) $(SITE_DIR) $(VENV_DIR)