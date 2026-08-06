# Using the functional conformity assurance framework

This section explains how the FCAF can be used. The framework's goal is to facilitate verification of the compliance of an EUDI-wallet implementation with the EUDI-wallet requirements.
The scope of coverage is limited to functional requirements. That does cover protocol specifications when interacting with peers in the ecosystem, credential formats and mandatory user interaction and functionality.
A production ready and compliant EUDI-wallet has to meet many other requirements. These requirements have to be covered elsewhere or with other frameworks.

## Audience
The FCAF in its current form is mainly intended for use by wallet providers implementing the EUDI-wallet requirements, labs and CABs testing those wallets, and related supervisors.

## FCAF structure
The FCAF consists of two main parts. The first part is test case specifications. The second part is test guidance.
For a compliant EUDI-wallet, both parts should be applied. Both parts are complementary and cover different aspects of the requirements for an EUDI-wallet.
As the FCAF is not a mandatory framework to use, anyone applying the FCAF may use alternative methods to verify compliance, either of parts or the whole of the FCAF.

## Test case specifications
The test case specifications describe methods to test individual requirements in a way that can be directly executed or implemented for use with automated test tooling.
Descriptions of test cases do not prescribe test tools or specific tooling. Each test case typically covers a single requirement that each EUDI-wallet must implement.

### Using the test case specifications


#### System under test
For the FCAF, only the Wallet Unit is considered the 'system under test' (SUT). By extension, some -- though surely not all -- of the functionality provided by the Wallet Provider is in scope for testing as well.
Other roles in the ecosystem are currently not in scope for testing by the FCAF, although these systems would need testing as well.

As system under test, the Wallet Unit is to be placed in a controlled environment. Peers in this environment interacting with the SUT are required to send specific messages and capture responses from the SUT.
A Wallet Unit is considered a "black box" and is tested without assumptions about, or required knowledge of, its inner workings.

The Wallet Unit, often referred to as just "Wallet", is to be tested in a controlled environment. Such environment is essential to assure any finding are objective, can be reproduced and can directly be related to the system under test.
This has numerous implications, many which will not be described here in the FCAF. Most is left up to the tester or a certification scheme. Some obvious items are listed, although this is not exhaustive.
* fixed versions of the wallet unit application, the underlying operating system and other relevant components.
* stable network connectivity, if applicable, including known correctly functioning routing, time- and DNS services.
* known test keys to use as trust anchors for relevant infrastructure components, such as the eIDAS trust lists and Wallet Provider. Note that some (negative) tests require specific non-compliant behaviour from peers, thus by implication cannot be executed with production systems using production keys.
* it is recommended to execute tests on various different devices from the range of supported devices and versions of operating system, platform, browser(s) and other relevant components. Such is out of scope of the FCAF though.
More information on conformance testing can be found in for example the ISO/IEC 9646 series.

#### Implementation Conformity Statement (ICS)
The implementer of a Wallet subject to testing has choices regarding various features of a compliant EUDI-wallet. Some functionality or items are optional under the eIDAS Regulation and related legislation. Other features are defined as recommended or optional in the underlying standards and technical specifications. If a feature is implemented, certain requirements often apply to the implementation of that feature.

Other than supported features, other implementation choices are relevant to be known when testing. This includes among others:
* cryptographic algorithms, protocols and schemes supported, if multiple acceptable variants exist.
* deployment names and identifiers that may occur in items like certificates and protocol messages.

As a result, not all conformity tests are applicable to each tested wallet. To capture these non-mandatory features and choices, an Implementation Conformity Statement (ICS) should be completed by the implementer.
A completed ICS can be used to select test cases that are applicable to the specific implementation of the SUT. The "Profile applicability" of a test case indicates whether a test case is applicable for non-mandatory features and can be matched against the ICS of the SUT.
Other elements of the ICS are input to test execution. Certain test cases describe items to be requested or parameters for constructs to be used.
The details from a completed ICS can thus be used to steer and configure test execution.

If an implementation supports multiple deployment settings or configurations, each matching a different ICS, it is the responsibility of the tester to execute tests for each valid configuration. A SUT has to meet the ICS, as that defines which requirements are relevant as part of evaluating compliance and what is tested for.

#### Test preparation
Before a Wallet is usable for an End-user, it typically has to go through various steps before it is operational. Such steps often include installation on a supported mobile device of choice and setting up local user authentication like fingerprint or PIN-code.
Other elements may have to be completed as well, depending upon implementation, such as configuring backup, capturing or setting revocation information, etc...

The FCAF makes several assumptions about what has been handled before test execution can commence. A number of generic items are part of preparation before test execution. It is left to a tester or test scheme to arrange for specifics, where applicable.
From the point of view of the FCAF, the relevant items to fulfil these assumptions are defined by a "default configuration". The majority of test cases are intended to work with one of the "default configurations" as a starting point. Deviations will be explicitly listed.

The tester has to set up and configure the SUT to meet the ICS, if applicable.

Finally, the tester may need to set up or configure the SUT for establishing trust with test systems. Note that this has two effects: the SUT needs to trust the test systems that act as peers during tests, and the test systems need to trust the SUT. Loading of trust anchors, cryptographic keys, certificates or specific identifiers may be necessary in both SUT and test systems.

#### Test execution
Tests are designed to be agnostic of the tools used. Tests as specified can be fully automated by a specialized tool or executed by the tester through manually selecting and crafting messages.

Whether using automated or manual tooling, the tester will have to operate the EUDI-wallet that is SUT. As implementations vary, the tester needs to be acquainted with the wallet's working, as test specifications only describe functionally what steps need to be performed. It is up to the tester to perform the applicable interactions with the SUT through interpretation or mapping for the specific wallet implementation being tested.

Test case specifications include pre-conditions, a test scenario and expected results. The tester will have to assure the preconditions are met, execute the steps in the test scenario and observe and evaluate to compare with expected results.
As instructions are functionally described, the tester will need to choose when options are presented. The test case specifications assume the tester chooses the logical path for an objective (e.g. presentation or issuance) and selects "defaults" where possible, unless a test scenario indicates otherwise. Choosing the logical path and "defaults" means choosing pre-selected options, heeding warnings, performing local authentication when prompted, and providing consent when asked, among other things.

Furthermore, the configuration should not be changed during test execution. Changes to the configuration of the underlying system (i.e. device, OS, or platform) or SUT, in particular those that are not part of regular usage, should not be needed. If such changes are necessary to continue during a test or achieve a pass, the test should be considered failed for the specific ICS/configuration.

Practical concerns may arise, hampering test execution. For example, a tester may need to enroll their face or fingerprint in a specific device, in order to perform local authentication. Or issuer systems are used that require specific credentials.
Such mechanisms are relevant for a comprehensive and realistic solution, that meets all requirements for an EUDI-wallet. It is out of scope of the FCAF how to handle with such situations, and whether or not certain specific modifications, workarounds or other deviations are acceptable or can otherwise be considered as without risk to compliance of the final solution as intended.

#### Test completion
Not all test case specifications describe actions until an entire use case is completed. When the end of a test scenario has been reached, and all (expected) results have been evaluated, a tester can continue and complete the use case.
As the FCAF defines test case specifications and not a certification scheme, no reporting instructions are included. It is up to a tester to capture execution, results and findings in an appropriate manner. Tests are designed to have one of three possible outcomes:
- Not applicable. In case a test case has a "profile applicability" that is not met by the ICS, the test is "not applicable" for the SUT.
- Test pass. The SUT passes the test, and is therefore compliant with the tested requirement, if the test scenario can be completed and all expected results are met.
- Test fail. If the SUT does not pass the test and the test is applicable, the test fails.
A SUT that passes all applicable tests is compliant with all tested requirements. That does not automatically imply the SUT is compliant. Other requirements, in particular those covered by the test guidance and any non-functional requirement, need to be assessed as well. Actual certification or another declaration of compliance is out of scope of the FCAF.

After completing a test, the tester should return the SUT to a neutral state before continuing to the next test. Most tests should not have any side effects and are intended to allow the SUT to return to a neutral state. However, this may vary depending on available credentials and the number of tests executed, as credentials may, for example, have a one-time-use policy.
