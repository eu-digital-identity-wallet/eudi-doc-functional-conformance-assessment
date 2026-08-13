# Using the Functional Conformance Assessment Framework

This section explains how to use the FCAF. The framework is intended to facilitate verification that an EUDI Wallet implementation complies with the EUDI Wallet requirements.
Its coverage is limited to functional requirements. These include protocol specifications for interactions with peers in the ecosystem, credential formats, and mandatory user interactions and functionality.
A production-ready and compliant EUDI Wallet must meet many other requirements. Those requirements must be covered elsewhere or by other frameworks.

## Audience

In its current form, the FCAF is mainly intended for Wallet Providers implementing the EUDI Wallet requirements, laboratories and conformity assessment bodies (CABs) testing those wallets, and the relevant supervisory bodies.

## FCAF structure

The FCAF consists of two main parts: test case specifications and test guidance.
Both parts should be applied when assessing a compliant EUDI Wallet. They complement each other and cover different aspects of the EUDI Wallet requirements.
Because use of the FCAF is not mandatory, anyone applying it may use alternative methods to verify compliance with parts of the FCAF or with the framework as a whole.

## Test case specifications

The test case specifications describe methods for testing individual requirements in a form that can be executed directly or implemented in automated test tooling.
The test case descriptions do not prescribe specific test tools or tooling. Each test case typically covers a single requirement that every EUDI Wallet must implement.

### Using the test case specifications

#### System under test

For the FCAF, only the Wallet Unit is considered the system under test (SUT). By extension, some, but not all, of the functionality provided by the Wallet Provider is also in scope for testing.
Other roles in the ecosystem are not currently in scope for FCAF testing, although those systems also need to be tested.

The SUT is placed in a controlled environment. Peers that interact with the SUT in this environment must send specific messages and capture responses from the SUT.
A Wallet Unit is considered a black box and is tested without assumptions about, or required knowledge of, its inner workings.

The controlled environment is essential to ensure that findings are objective, reproducible, and directly attributable to the SUT.
This has numerous implications, many of which are not described in the FCAF. Most are left to the tester or a certification scheme. The following list provides non-exhaustive examples:

- fixed versions of the Wallet Unit application, the underlying operating system, and other relevant components;
- stable network connectivity, if applicable, including known and correctly functioning routing, time, and DNS services;
- known test keys used as trust anchors for relevant infrastructure components, such as eIDAS trust lists and the Wallet Provider. Some negative tests require specific non-compliant behaviour from peers and therefore cannot be executed with production systems using production keys;
- execution of tests on different devices from the supported range, and on different versions of the operating system, platform, browsers, and other relevant components. This is outside the scope of the FCAF.

More information on conformance testing is available in the ISO/IEC 9646 series.

#### Implementation Conformance Statement (ICS)

The implementer of a Wallet under test can make choices about various features of a compliant EUDI Wallet. Some functionality or items are optional under the eIDAS Regulation and related legislation. Other features are defined as recommended or optional in the underlying standards and technical specifications. When a feature is implemented, specific requirements often apply to its implementation.

In addition to supported features, other implementation choices must be known when testing. These include:

- supported cryptographic algorithms, protocols, and schemes, if multiple acceptable variants exist;
- deployment names and identifiers that may occur in items such as certificates and protocol messages.

As a result, not all conformance tests apply to every Wallet under test. To capture these non-mandatory features and choices, the implementer should complete an Implementation Conformance Statement (ICS).
A completed ICS can be used to select the test cases that apply to the specific implementation of the SUT. The `Profile applicability` section of a test case indicates whether the test case applies to non-mandatory features and can be matched against the SUT's ICS.
Other elements of the ICS provide input for test execution. Certain test cases describe items to be requested or parameters for constructs to be used.
The details in a completed ICS can therefore be used to guide and configure test execution.

If an implementation supports multiple deployment settings or configurations, each matching a different ICS, the tester is responsible for executing tests for every valid configuration. A SUT must conform to its ICS because the ICS defines which requirements are relevant to the compliance evaluation and what is tested.

#### Test preparation

Before a Wallet can be used by an End-user, it typically must pass through several steps. These often include installation on a supported mobile device and configuration of local user authentication, such as a fingerprint or PIN.
Other steps may also be required, depending on the implementation, such as configuring backups or capturing or setting revocation information.

The FCAF makes several assumptions about what has been completed before test execution begins. A number of generic items are part of test preparation. The tester or test scheme is responsible for arranging the details, where applicable.
From the FCAF perspective, the relevant items that fulfil these assumptions are defined by a `default configuration`. Most test cases are intended to use one of the default configurations as their starting point. Any deviations are listed explicitly.

The tester must set up and configure the SUT to match the ICS, if applicable.

Finally, the tester may need to configure the SUT to establish trust with test systems. This has two effects: the SUT must trust the test systems acting as peers, and the test systems must trust the SUT. Trust anchors, cryptographic keys, certificates, or specific identifiers may need to be loaded into both the SUT and the test systems.

#### Test execution

Tests are designed to be independent of the tools used. The specified tests can be fully automated by specialised tooling or executed manually by a tester who selects and crafts messages.

Whether automated or manual tooling is used, the tester must operate the EUDI Wallet that is the SUT. Because implementations vary, the tester must understand how the Wallet works. The test specifications describe the required steps in functional terms, and the tester must interpret or map them to the specific Wallet implementation under test.

Test case specifications include preconditions, a test scenario, and expected results. The tester must ensure that the preconditions are met, execute the steps in the test scenario, and observe and evaluate the expected results.
Because the instructions are described in functional terms, the tester must choose among any options presented. Unless a test scenario states otherwise, the test case specifications assume that the tester chooses the logical path for an objective, such as presentation or issuance, and selects defaults where possible. Choosing the logical path and defaults includes choosing preselected options, heeding warnings, performing local authentication when prompted, and providing consent when requested.

The configuration should not change during test execution. Changes to the configuration of the underlying system, such as the device, operating system, or platform, or to the SUT itself should not be necessary, particularly when they are not part of regular use. If such changes are necessary to continue a test or obtain a passing result, the test should be considered failed for the specific ICS or configuration.

Practical concerns may impede test execution. For example, a tester may need to enrol a face or fingerprint on a specific device to perform local authentication, or an issuer system may require specific credentials.
Such mechanisms are relevant to a comprehensive and realistic solution that meets all EUDI Wallet requirements. How to handle these situations is outside the scope of the FCAF, including whether specific modifications, workarounds, or other deviations are acceptable or can be considered not to pose a compliance risk to the intended final solution.

#### Test completion

Not all test case specifications describe actions through to completion of an entire use case. When the end of a test scenario is reached and all expected results have been evaluated, the tester can continue and complete the use case.
Because the FCAF defines test case specifications rather than a certification scheme, it does not include reporting instructions. The tester is responsible for recording test execution, results, and findings appropriately. Tests are designed to have one of three outcomes:

- Not applicable. If a test case has a `Profile applicability` condition that is not met by the ICS, the test is not applicable to the SUT.
- Test pass. The SUT passes the test and is therefore compliant with the tested requirement if the test scenario can be completed and all expected results are met.
- Test fail. If the SUT does not pass an applicable test, the test fails.

A SUT that passes all applicable tests complies with all tested requirements. This does not automatically mean that the SUT is fully compliant. Other requirements, particularly those covered by the test guidance and any non-functional requirements, must also be assessed. Certification or another declaration of compliance is outside the scope of the FCAF.

After completing a test, the tester should return the SUT to a neutral state before proceeding to the next test. Most tests should have no side effects and are intended to allow the SUT to return to a neutral state. However, this may vary according to the available credentials and the number of tests executed because credentials may, for example, have a one-time-use policy.
