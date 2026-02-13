# Test Specification Template

This template defines the structure for **functional test specifications** used in the FCAF.
Test specifications are intended for **automated or semi-automated** execution where possible.

## Template fields

A Test Case specification SHOULD include:

### 1. Test case identifier
- **Test case ID**: unique identifier following the FCAF naming convention.

### 2. Objective
- Short statement of what is being validated.

### 3. References
- References to requirements and sources (CIRs, ETSI, ISO, OIDF, IETF, etc.).

### 4. Profile applicability
- Applicable profile(s), if any.
- Rules for when the test is **Not Applicable**.

### 5. Preconditions
- Required initial state and configuration.

### 6. Test scenario
For each step:
- Step ID
- Description
- Inputs/configuration (if applicable)

### 7. Expected results
- Expected outcomes per step and pass/fail criteria.