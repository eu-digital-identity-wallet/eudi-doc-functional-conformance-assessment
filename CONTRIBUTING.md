# CONTRIBUTING

Thank you for your interest in the **Functional Conformance Assessment Framework (FCAF)**.

This document describes the contribution and review model for this repository.

Please note that the FCAF is **work in progress** and currently in a **draft baseline phase (v0.1.x)**.

---

## ⚠️ Current status (important)

This repository contains **draft FCAF content** intended to:

- establish a baseline of test specifications,
- enable early review and contribution,
- support iterative refinement, and
- progressively converge towards an implementation-ready release baseline (**v1.0.0**).

Content may be incomplete, inconsistent, or not yet implementation-ready.

## 1) Purpose & scope

This repository hosts documentation and artefacts for the **Functional Conformance Assessment Framework (FCAF)**.

The FCAF is intended to:

- support and harmonise functional conformance testing under the applicable **Implementing Regulations**,
- improve **interoperability** across EUDI Wallet implementations,
- provide reusable artefacts (test specifications, test books, configuration data, and guidance)
  for use by **Conformity Assessment Bodies (CABs)** and related stakeholders.

At this stage, the content is **not normative** and does not replace, amend, or reinterpret
any legally binding text.

> Normative requirements remain exclusively defined by the applicable Implementing
> Regulations and referenced legal acts.

---

## 2) Contribution model

This repository adopts an **open contribution model**.

Contributions are made via:

- GitHub issues for:
  - content clarifications,
  - editorial improvements,
  - error corrections,
  - technical questions and alignment discussions.

- Pull requests for:
  - proposed text changes,
  - improvements to test cases and other FCAF content,
  - refinements and corrections.

Contributions are expected to be:

- focused,
- well-structured,
- and aligned with the overall objectives of the FCAF.

Contributions do not directly assign a maturity stage; progression through stages is determined through the review and governance process.

---

## 3) Review and refinement model

Framework content and test cases are refined through a staged maturity model.

Content is initially created or updated in the **submitted** stage, which represents ongoing work and the latest working draft. At this stage, content may contain inconsistencies or gaps and is not yet considered implementation-ready.

Through structured review by designated reviewers, content progresses to the **reviewed** stage. At this point, it is technically correct, internally consistent, and implementable as a black-box test. Reviewed content represents reference-quality test cases, although it may not yet be fully consolidated across all applicable specifications, profiles, and regulatory layers.

A selected subset of reviewed content may then be promoted to the **release candidate (RC)** stage. At this stage, content is sufficiently consolidated across applicable layers, including standards, profiles, and Implementing Acts, and forms the first usable baseline for implementation. Release candidates are used by stakeholders for implementation, testing, and evaluation, and may be iterated based on feedback.

Finally, content is promoted to a **released baseline** once it is considered sufficiently stable and usable. This decision is based on implementation feedback, resolution of critical issues, and endorsement by relevant governance bodies (e.g. EDICG).

The lifecycle of content is therefore:

submitted → reviewed → release candidate → released baseline

The maturity stage of content is not expressed within individual test cases, but is managed through the review process and repository workflow.

---

## 4) Review governance

The FCAF follows a structured governance model for the promotion of content between maturity stages.

- Contributions are open to all stakeholders and may be proposed at any stage.
- However, promotion of content between stages is controlled.

**Designated reviewers** act as the quality gate and are responsible for:

- assessing correctness, consistency, and implementability,
- determining when content can be considered reviewed,
- promoting content from the submitted stage to the reviewed stage.

The **release manager** (European Commission) is responsible for:

- selecting content for release candidates,
- promoting content from the reviewed stage to the release candidate stage,
- deciding on the release of a baseline based on stakeholder feedback.

Release candidate content is presented to relevant governance bodies (e.g. EDICG / Cooperation Group) for discussion and feedback. Endorsement by these bodies is required for promotion to a released baseline.

This model ensures:

- open contribution,
- controlled quality assurance,
- and structured convergence towards a stable baseline.

---

## 5) Code of conduct

All interactions in this repository are expected to be:

- respectful,
- constructive,
- focused on technical and editorial substance.

Disagreement is normal; personal remarks are not.
Concrete proposals, references, and examples are strongly encouraged.

---

## 6) Editorial principles

Contributions should:

- improve **clarity, traceability, implementability, and interoperability**
- remain aligned with the **scope and intent** of the applicable Implementing Regulations

Use **RFC 2119 / RFC 8174 keywords** (MUST, SHALL, SHOULD, MAY) **only** when:

- quoting normative text, or
- precisely tracking regulatory language

Otherwise, use plain, descriptive language.

---

## 7) Versioning and releases

The FCAF follows a versioning model that reflects both **coverage** (vX.Y.Z) and **maturity** (beta, release candidate, released baseline). Versioned releases are managed through GitHub tags, which represent specific snapshots of the framework at defined maturity stages.

### Submitted stage

The submitted stage represents ongoing work and reflects the latest working draft. It is not maintained as a dedicated version within the versioning scheme, as content is expected to evolve following review by designated reviewers. Content at this stage is not considered implementation-ready.

### Reviewed stage (beta)

Reviewed content may be published as **beta versions**:

- **vX.Y.Z-beta.n**

Beta versions represent:

- reviewed content,
- technically sound and implementable in isolation,
- not yet fully consolidated across all applicable specifications, profiles, and regulatory layers.

Beta versions are typically created from the **reviewed branch** and provide early visibility for implementers and reviewers.

---

### Release candidate (RC)

Release candidates are published as:

- **vX.Y.Z-rc.n**

Release candidates represent:

- content consolidated across applicable layers (standards, profiles, Implementing Acts),
- the first usable baseline for implementation,
- content prepared for stakeholder validation and governance feedback.

Release candidates are typically created from the **rc branch** and may be iterated (e.g. rc.1, rc.2) based on feedback from stakeholders, including EDICG.

---

### Released baseline

Released baselines are published as:

- **vX.Y.Z**

Released baselines represent:

- stable and sufficiently validated content,
- suitability for implementation and conformance assessment,
- endorsement by relevant governance bodies including EDICG.

Released baselines are created from the **main branch** following successful validation and endorsement.

---

### Relationship between maturity stages and versions

The relationship between maturity stages and versioning is as follows:

```text
submitted  → not versioned
reviewed   → vX.Y.Z-beta.n
rc         → vX.Y.Z-rc.n
released   → vX.Y.Z
```

Version numbers (vX.Y.Z) reflect the scope and coverage of the framework, while suffixes (beta, rc) reflect the maturity of the content.

### v0.x.y and v1.0.0

The **v0.x.y series** represents partial coverage of the overall framework and ongoing iterative refinement.

The **v1.0.0 release** will represent the first full-scope baseline that is:

- stable,
- validated to a sufficient degree, and
- suitable as a certification-relevant baseline.

The target is to progress towards a release candidate (RC) by mid-July, subject to stakeholder participation.

---

### Release and evolution model

Contribution instructions, issue templates, and review processes are available in this repository and evolve alongside the FCAF.

The FCAF is developed through **continuous iterative refinement (v0.1.x)** and presented regularly in focus meetings on certification to gather feedback and inform subsequent refinements.

As the FCAF aims to provide a high level of rigor in assessing functional requirements mandated by the Regulation, it is progressively refined until a sufficient level of maturity is achieved.

The **v1.0.0 release** represents the first implementation-ready baseline for certification, subject to validation against defined acceptance criteria.

After **v1.0.0**, changes will be managed in a controlled manner:

- consolidated changelogs will be published,
- the potential impact on previously completed conformity assessments will be assessed,
- substantive or breaking changes will be discussed with Member States prior to inclusion.

Breaking changes after **v1.0.0** are not expected.

This approach supports transparent evolution of the framework and, where necessary, the definition of appropriate transition or coexistence measures.

---

## 8) Licensing & IPR

All content in this repository is subject to the repository [LICENSE](LICENSE.md).

---

## 9) Contact

Questions about scope or process should be raised via:

- GitHub issues, or
- established coordination channels associated with the FCAF work

---

## What happens next

- **v0.0.x** – Bootstrap phase (completed)
- **v0.1.x** – Continuous iteration and refinement of draft artefacts
- **v1.0.0** – Implementation-ready baseline for certification

Indicative evolution of the framework is described in:
[roadmap.md](docs/overview/roadmap.md)

---

Thank you for your contribution to the FCAF.