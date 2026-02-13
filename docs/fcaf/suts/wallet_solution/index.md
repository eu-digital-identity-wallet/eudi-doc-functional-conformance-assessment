# Wallet Solution (SUT)

The **Wallet Solution** is the initial System Under Test (SUT) for the FCAF.

Functional conformance testing of the Wallet Solution covers:

- **External interfaces** with ecosystem peers (Issuers, Verifiers, Infrastructure Components); and
- **Internal functionality** required by regulations and referenced technical standards, including behaviour that cannot be fully proven via standardised external interfaces.

## Test Classes within the Wallet Solution

To keep scope manageable and navigable, the Wallet Solution SUT is subdivided into classes:

- **Wallet_Verifier**: presentation interface and related functionality
- **Wallet_Issuer**: issuance/provisioning interface and related functionality
- **Wallet_Infrastructure**: interfaces to infrastructure components
- **Wallet_UI**: user-facing functionality that is not fully testable via standardised external interfaces