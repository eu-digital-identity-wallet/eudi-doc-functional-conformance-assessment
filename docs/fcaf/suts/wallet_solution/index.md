# Wallet Solution (SUT)

The **Wallet Solution** is the initial System Under Test (SUT) for the FCAF.

Functional conformance testing of the Wallet Solution covers:

- **External interfaces** with ecosystem peers (PID Providers, Attestation Providers, Relying Parties, Infrastructure Components); and
- **Internal functionality** required by regulations and referenced technical standards, including behaviour that cannot be fully proven via standardised external interfaces.

## Test Classes within the Wallet Solution

To keep scope manageable and navigable, the Wallet Solution SUT is subdivided into classes:

- **WalletSolution_RelyingParty**: presentation interface and related functionality
- **WalletSolution_PidProvider**: issuance/provisioning interface and related functionality
- **WalletSolution_AttestationProvider**: issuance/provisioning interface and related functionality
- **WalletSolution_Infrastructure**: interfaces to infrastructure components
- **WalletSolution_UI**: user-facing functionality that is not fully testable via standardised external interfaces