# European Digital Identity - Functional Conformance Assessment Framework (FCAF)

This repository contains the **European Digital Identity (EUDI)
Functional Conformance Assessment Framework (FCAF)** and serves as the
**authoritative publication repository** for released versions of the
framework.

The latest **authoritative version** is available via the\
[GitHub Releases
page](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/releases).

An **online rendered version** of the documentation will be published at:
https://conformance.eudi.dev (in W8 2026).

## Release & Publication Workflow

Releases are **tag-driven**.

Create and push a release tag:

``` bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

This triggers the CI workflow which:

1.  Builds and **versions documentation via mike**
2.  Publishes HTML to **GitHub Pages**
3.  Generates **PDF artefacts** using Pandoc + Eisvogel
4.  Creates a **ZIP archive** of PDFs
5.  Attaches PDFs and ZIPs to the **GitHub Release**

Workflow definition:

``` text
.github/workflows/pages.yml
```

The CI pipeline uses the **same Makefile targets** as local development,
ensuring:

-   reproducible builds
-   single source of truth for build logic
-   consistent local ↔ CI behaviour

## Contributing

See the [CONTRIBUTING](./CONTRIBUTING.md) file for details.

## Authors

See the list of [contributors](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/graphs/contributors)
who participated in this project.

## Licence

See the [LICENCE](./LICENCE.md) file for details.

## [European Commission website](https://commission.europa.eu/index_en)

* [Contact the European Commission](https://commission.europa.eu/about-european-commission/contact_en)
* [Follow the European Commission on social media](https://european-union.europa.eu/contact-eu/social-media-channels_en#/search?page=0&institutions=european_commission)
* [Resources for partners](https://commission.europa.eu/resources-partners_en)

## Working locally

### Prerequisites

#### For HTML docs (MkDocs)

-   Python **3.11+**
-   `make`
-   Git

Install Python dependencies via:

``` bash
make install_deps
```

#### For PDF generation (Pandoc + XeLaTeX + Mermaid)

Required tooling:

-   **Pandoc**
-   **TeX Live with XeLaTeX**
    -   `texlive-xetex`
    -   `texlive-latex-extra`
    -   fonts packages
-   **Node.js + npm**
-   **Mermaid CLI** (`@mermaid-js/mermaid-cli`, provides `mmdc`)
-   **Headless browser for Mermaid rendering**
    -   Linux: `chromium` (recommended)
    -   macOS: `chromium` or Puppeteer‑managed Chromium
-   **SVG conversion tools**
    -   `librsvg2-bin` → provides `rsvg-convert` (required for SVGs in
        PDF)
    -   *(optional)* `inkscape`

> Mermaid CLI internally uses a headless browser.
> If `mmdc` works directly on your machine, the PDF pipeline should work
> too.

### Installation examples

#### Ubuntu / Debian

``` bash
sudo apt-get update
sudo apt-get install -y   make git python3 python3-venv python3-pip   pandoc   texlive-xetex texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra   librsvg2-bin   nodejs npm   chromium   inkscape

sudo npm i -g @mermaid-js/mermaid-cli
```

Optional emoji support in PDFs:

``` bash
sudo apt-get install -y fonts-noto fonts-noto-color-emoji
```

#### macOS (Homebrew)

``` bash
brew install git make python@3.11 pandoc mactex node chromium librsvg inkscape
npm i -g @mermaid-js/mermaid-cli
```

> `mactex` is large but the most reliable way to obtain XeLaTeX.

### Quick sanity checks

``` bash
python3 --version
pandoc --version
xelatex --version
mmdc --version
rsvg-convert --version
```

### Setup

```bash
make install_deps
```

### Run the docs site

```bash
make local_serve
```

### Run the versioned site locally (mike)

```bash
make local_serve_versions
```

### Build the PDF

```bash
make pdf VERSION=0.0.1
```

The generated PDF will be in:

- `build/pdf/fcaf-framework.pdf`