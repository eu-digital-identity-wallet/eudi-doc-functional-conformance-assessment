# Test Specification Template

This template defines the structure for **functional test specifications** used in the FCAF.
Test specifications are intended for **automated or semi-automated** execution where possible.

## Template fields

A Test Case specification SHOULD include:

  1. Test case identifier
  2. Test objective
  3. References
  4. EUDI-wallet relevancy
  5. Profile applicability
  6. Technology
  7. Preconditions
  8. Test scenario
  9. Expected results
  10. Comment

### 1. Test case identifier

- **Test case ID**: unique identifier following the FCAF naming convention.

### 2. Objective

- Short statement of what is being validated.

### 3. References

- References to requirements and sources (CIRs, ETSI, ISO, OIDF, IETF, etc.).

### 4. Profile applicability

- Applicable profile(s), if any.
- Rules for when the test is **Not Applicable**.

### 5. EUDI-wallet relevancy

- Indicators on relevance to EUDI-wallet ecosystem.

### 6. Technology

- The specific technology, credential format, or transmission mechanism variant the
  test targets (e.g. `Credential in SD-JWT VC format`, `Credential in mdoc format`,
  `Presentations via Redirects`, `Presentations via the W3C Digital Credentials API`).

- This is the discriminator between sibling test cases that share an objective but
  differ by technology (for example the SD-JWT VC and mdoc variants of the same query).

- Omit the field only where the test is technology-agnostic.

### 7. Preconditions

- Required initial state and configuration.

### 8. Test scenario

For each step:

- Step ID
- Description
- Inputs/configuration (if applicable)

### 9. Expected results

- Expected outcomes per step and pass/fail criteria.

### 10. Comments

- Optional comment(s)
