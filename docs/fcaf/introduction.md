# Introduction

The European Commission adopted [Commission Implementing Regulation (CIR) (EU) 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402981) on the certification of European Digital Identity (EUDI) Wallets.
This Regulation establishes the **baseline framework for certification**, including requirements related to cybersecurity, privacy, and operational assurance.  
It also requires conformity assessment of **functional requirements** defined by the following CIRs (see [Annex III of CIR (EU) 2024/2981](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402981#anx_III)):

- **Integrity and core functionalities** – CIR (EU) 2024/2979  
- **Protocols and interfaces** – CIR (EU) 2024/2982  
- **Person identification data and electronic attestations of attributes** – CIR (EU) 2024/2977  

To harmonise the functional conformity assessment required during certification, the European Commission is establishing a **Functional Conformance Assessment Framework (FCAF)** for the following reasons:

- Preventing market fragmentation  
- Ensuring a uniform high level of robustness and security  
- Reducing certification costs and duplication  
- Strengthening EU-wide cyber resilience  
- Enabling coherent and comparable conformance testing  
- Increasing transparency and auditability  
- Facilitating interoperability across implementations and Member States  

The FCAF provides a **shared, transparent, and reusable set of framework content and test cases** that can be applied consistently by **Conformity Assessment Bodies (CABs)**, test laboratories, wallet providers, tool vendors, and other stakeholders.

The FCAF aims to:

- Provide a common set of test cases, test specifications, configuration data, and profiles enabling CABs and test laboratories to evaluate functional and functional-security requirements  
- Define structured test specifications (e.g. preconditions, steps, expected results) that are tool-agnostic and may be executed manually or via externally developed tooling  
- Build upon a gap analysis of existing test specifications for essential standards and technical specifications relevant to EUDI Wallet solutions (see [Focus X document](https://ec.europa.eu/digital-building-blocks/wikis/spaces/CG/pages/767071732/Topic+X+-+Conformance+testing+for+functional+requirements))  
- Draw methodological inspiration from ISO/IEC 18013-6  
- Be developed in collaboration with Standards Development Organisations (SDOs)  
- Be governed by the European Commission, in cooperation with Member States through the EUDI Wallet Cooperation Group (EDICG)

## Background

This work relates to functional conformance testing under the EUDI Wallet certification framework as established by **CIR (EU) 2024/2981**.

The objective is to test:

- combinations of technical provisions from CIRs and referenced standards that together constitute the **functional requirements** EUDI Wallets are expected to support,  
- **production-like use** of these technical provisions, including relevant functional security requirements, and  
- only those functional requirements from standards that are **actually used by EUDI Wallets**.  

Earlier work on the FCAF resulted in the publication of the **Focus X document (v1)**, which:

- assessed existing standards, test specifications, and tools relevant for functional conformance testing,  
- identified gaps in current test specifications, and  
- outlined actions required to achieve comprehensive test coverage and interoperability between Wallet Solutions.  

The **Focus X document (v1)** concluded that significant gaps exist in current test specifications for functional requirements defined in relevant CIRs and referenced standards.

To support harmonised evaluation of functional requirements during certification of EUDI Wallet solutions, a **common and structured testing methodology** is required. The FCAF addresses this need.

## Functional conformance testing

Functional conformance testing aims to demonstrate that an implementation behaves as required by applicable standards, technical specifications, profiles, and regulatory requirements, and that it can interoperate within the EUDI Wallet ecosystem.

### Conceptual coverage

Functional conformance testing typically includes:

- **External interface testing**: behaviour observable at standardised interfaces (e.g. Wallet Solution ↔ PID/Attestation Provider, Wallet Solution ↔ Verifier).  

- **Internal functional requirements**: behaviour mandated by regulations or technical standards that may not be fully testable via standardised external interfaces, and therefore may require structured manual testing or observation of behaviour (e.g. a wallet requesting user consent before sharing data with a Verifier).  

### Rationale

Functional conformance testing is necessary:

- because it is not feasible to test all permutations in a many-to-many ecosystem  
  (Wallets × PID/Attestation Providers × Verifiers),  
- to enable seamless and consistent operation of the ecosystem, which is essential for adoption and long-term success, and  
- to achieve interoperability across implementations and Member States.  

### Distinction from other testing

Functional conformance testing is distinct from:

- **Sandbox or "happy-flow" interoperability testing**, which is primarily used during development or test events,  
- **non-functional testing**, such as performance, scalability, penetration testing, or availability testing, and  
- **operational readiness testing**, including release management, monitoring, and incident response.  

The FCAF focuses on providing **repeatable and comparable functional test cases**.

## Scope

The FCAF supports testing of **functional and functional-security requirements relevant within the EUDI Wallet ecosystem** by providing test objectives and structured test cases for:

- wallet **external interfaces** with PID/Attestation Providers, Verifiers, and infrastructure components, and  
- wallet **internal functionality** where functional requirements exist but cannot be validated solely through an external interface.  

The FCAF is composed of the following core elements:

- **Test specifications**: structured definitions of primarily automatable tests, including inputs, steps, and expected results  
- **Test books**: structured collections of manual or non-automatable test cases (e.g. user-facing flows)  
- **Traceability mappings**: mappings between test cases and functional requirements defined in CIRs and relevant standards or technical specifications  
- **Application guidance**: guidance for CABs on how to apply the framework content consistently and how to report outcomes (e.g. Implementation Conformance Statement (ICS))  
- **Catalogue of externally developed testing tools**: a curated and non-exhaustive overview of third-party tools that may support execution or automation of FCAF test specifications, without the FCAF itself providing or mandating specific tooling  

Functional conformance testing is one component of national EUDI Wallet certification schemes established by Member States.

The FCAF defines **test cases addressing functional requirements** as required by the Regulation. Additional certification components, as defined in **CIR (EU) 2024/2981**, must be considered to achieve full certification.

## Out of scope

The FCAF addresses functional conformance testing only. It therefore excludes aspects of EUDI Wallet certification and evaluation that are not expressed as functional or functional-security requirements testable through functional conformance testing.

The FCAF does **not** cover certification activities related to:

- **Cybersecurity assurance**, including resistance to attacks, vulnerability management, secure development practices, and other security evaluation activities defined outside functional conformance  
- **Procedural or operational assurance**, such as organisational controls, lifecycle governance, incident handling, monitoring, and certification-scheme-specific operational processes  
- **Privacy and data protection assurance**, except where privacy requirements are explicitly formulated as functional or functional-security requirements that can be evaluated through functional conformance testing  

These aspects are addressed through **separate assurance and certification processes** defined in applicable legislation and certification schemes.

The FCAF does **not** include:

- **Non-functional testing**, such as performance, scalability, availability, or penetration testing  
- **Operational or production-readiness assessments**, including deployment validation, monitoring capability, or service management preparedness  

The FCAF defines test specifications, supporting framework content, and application guidance, but it does **not**:

- provide, mandate, or maintain testing tools or execution environments, or  
- prescribe specific automation frameworks for running the defined tests  

Execution tooling may be developed externally and used by CABs, test laboratories, or other implementers.

## Roadmap (Indicative)

> ⚠️ This roadmap is indicative and subject to change.

The roadmap provides a **high-level orientation only** and should not be interpreted as a binding delivery plan.

From version **v0.1.0 onwards**, the FCAF follows an **iterative delivery model**:

- Framework content and test cases are published early as **draft baseline content**  
- Content is refined incrementally through:
  - structured review,  
  - issue tracking, and  
  - pull requests  

The **v0.x.y series represents continuous iteration**, not discrete feature-complete releases.  
Maturity is reflected through staged progression (reviewed → release candidate → released baseline) and corresponding versioned releases.

While individual releases in the **v0.x.y series** provide usable and implementation-ready subsets of functionality, they represent **partial coverage** of the overall framework.

These releases are intended to support implementation, testing, and early validation. The **v1.0.0 release** will represent the first full-scope, sufficiently consolidated baseline suitable for certification.

terations of the core team are organised around the key functional areas outlined in the scope overview above.

Work progresses iteratively across these areas, with a **primary focus typically applied in the following order**:

- **Presentation flows** (e.g. OID4VP, HAIP, ISO/IEC 18013-5/-7, ETSI profiles)  
- **Issuance flows** (e.g. OID4VCI, HAIP, ETSI profiles)  
- **Credential formats** (e.g. SD-JWT VC, ISO mdoc, ETSI profiles)  
- **Trust and integrity mechanisms** (e.g. WUA/WIA, trust lists, verifier certificates, ETSI alignment)  
- **Qualified signatures and advanced use cases** (e.g. rQES, ETSI alignment)  

These areas are **not addressed strictly sequentially**. Instead:

- multiple areas are developed in parallel,  
- progress varies depending on complexity and dependencies, and  
- feedback from implementation and review continuously influences prioritisation.  

In particular:

- **Data models** (e.g. PID, EEA) are developed in parallel with presentation and issuance flows, and  
- **Regulatory alignment** (e.g. Implementing Acts) is progressively integrated as part of later consolidation stages.  

The scope overview reflects the **current status of coverage and progress** across these areas and should be read as a snapshot of ongoing work rather than a strictly sequential plan.

This progression supports incremental consolidation across specifications, profiles, and regulatory layers.

```mermaid
timeline
    title FCAF Roadmap (Indicative – Maturity Progression)

    section Foundation (v0.0.x)
        Completed : Initial baseline (GitHub, MkDocs)
                            : Framework structure and test architecture

    section Iterative development (v0.1.x)
        Ongoing : Incremental delivery of functional areas
                : Continuous review and refinement
                : Partial but usable coverage

    section Release candidate
        mid-July : Consolidated baseline (RC)
                 : Ready for validation and pilot use

    section Validation and governance
        September : EDICG focus meeting
                    : Review of RC and stakeholder feedback

    section Released Baseline (v1.0.0)
        After endorsement : First full-scope baseline
                : Suitable for certification use
```