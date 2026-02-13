# EUDI Functional Conformance Assessment Framework (FCAF)

This repository contains the **European Digital Identity (EUDI)
Functional Conformance Assessment Framework (FCAF)** and serves as the
**authoritative publication repository** for released versions of the
framework.

The latest **authoritative version** is available via the\
[GitHub Releases
page](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/releases).

An **online rendered version** of the documentation is published at:
https://conformance.eudi.dev

The documentation is:

-   built using **MkDocs (Material theme)**
-   versioned using **mike**
-   published via **GitHub Pages**
-   packaged into **PDF and ZIP release artefacts** using **Pandoc +
    Eisvogel**

------------------------------------------------------------------------

# Repository Structure

``` text
/
├── docs/                  ← Documentation source
│   ├── index.md           ← Website entry page
│   ├── fcaf/              ← FCAF specification content
│   └── media/             ← Images and static assets
│
├── mkdocs.yml             ← MkDocs configuration
├── requirements.txt       ← Python dependencies
├── Makefile               ← Unified local + CI build interface
│
├── build/                 ← Generated artefacts (git-ignored)
│   ├── pdf/
│   └── dist/
│
├── .github/workflows/
│   └── pages.yml          ← Release & publication workflow
│
└── README.md
```

> Generated directories such as `site/`, `build/`, `.venv/`, and
> `.cache/` are intentionally excluded from version control.

------------------------------------------------------------------------

# Local Development

The repository provides a **Makefile as the primary entry point** for
local development and CI. Using the Makefile ensures a consistent
environment and reproducible builds.

## 1. Install dependencies

``` bash
make install_deps
```

This will:

-   create a local Python virtual environment in `.venv`
-   install all dependencies from `requirements.txt`

------------------------------------------------------------------------

## 2. Preview documentation locally (live reload)

``` bash
make local_serve
```

The documentation will be available at:

    http://127.0.0.1:8000/

Changes under `docs/` reload automatically.

------------------------------------------------------------------------

## 3. Build the static HTML site

``` bash
make mkdocs
```

The generated site is written to:

``` text
site/
```

------------------------------------------------------------------------

## 4. Preview versioned documentation (mike)

``` bash
make local_serve_versions
```

This simulates the structure used on GitHub Pages:

    /0.0.1/
    /latest/

------------------------------------------------------------------------

## Direct MkDocs usage (optional)

Advanced users may run MkDocs commands directly **inside the virtual
environment**:

``` bash
mkdocs serve
mkdocs build
```

However, the **Makefile targets are the supported entry points** and
should be preferred.

------------------------------------------------------------------------

# PDF Generation (optional locally)

PDF generation requires:

-   **Pandoc**
-   **LaTeX (xelatex)**

Build PDFs:

``` bash
make pdf VERSION=0.0.1
```

Output:

``` text
build/pdf/
```

Create ZIP archive:

``` bash
make dist VERSION=0.0.1
```

Output:

``` text
build/dist/
```

> In CI, Pandoc and LaTeX are installed automatically.
> Local PDF generation is optional.

------------------------------------------------------------------------

# Release & Publication Workflow

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

------------------------------------------------------------------------

# Contributing

See the [CONTRIBUTING](./CONTRIBUTING.md) file for details.

------------------------------------------------------------------------

# Authors

See the list of [contributors](https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment/graphs/contributors)
who participated in this project.

------------------------------------------------------------------------

# Licence

See the [LICENCE](./LICENCE.md) file for details.

------------------------------------------------------------------------

# [European Commission website](https://commission.europa.eu/index_en)

* [Contact the European Commission](https://commission.europa.eu/about-european-commission/contact_en)
* [Follow the European Commission on social media](https://european-union.europa.eu/contact-eu/social-media-channels_en#/search?page=0&institutions=european_commission)
* [Resources for partners](https://commission.europa.eu/resources-partners_en)

