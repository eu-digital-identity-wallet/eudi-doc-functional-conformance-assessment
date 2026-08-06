# Default items

The following define various SUT configurations, credentials and trust anchors used throughout the test case specifications.
These definitions are intentionally logical rather than physical: they describe required structures and characteristics, but not specific values. The tester or test tooling supplies concrete values for execution.

### Default configurations
The following properties are defined for a SUT (EUDI-wallet unit). These are assumed to be realized in the SUT when the default configuration is used.

#### `default_configuration_A`

| Property | Setting, contents or value |
| --- | --- |
| App software | Installed on (mobile) device. |
| App permissions | All relevant permissions granted to the Wallet App as per instructions from Wallet Provider. |
| Peripheral and sensors activated | Any companion hardware or settings of relevant sensors (NFC, BLE, USB, ...) are connected and activated, if applicable. |
| App personalization | App instance is personalized, has local authentication configured and is registered with Wallet Provider, if applicable. |
| WSCA/WSCD | The WSCA/WSCD of the Wallet Unit is set up, linked to the Wallet Instance and available for usage |
| App localization | App is configured to a supported language. |
| EUDI-wallet state | Valid. That means that as per EUDI-wallet specifications, the wallet has a valid PID, is active and has not been revoked. |
| OS & platform | Software of the underlying system (test apparatus) is installed, configured and ready for use. |
| Complementary software | Software such as a compliant browser (user agent) is installed and ready for use. |
| Consent defaults | No preregistered consent for specific Relying Parties, Credentials or Attributes. |
| Stored credentials | The Wallet Unit has been issued with the following credentials, that are still valid: `default_credential_A`, `default_credential_B` and `default_credential_C`. |
| Network connectivity | Data connectivity is available and unrestricted. In case any filtering is applied for an isolated test network, all dependencies (DNS, NTP, ...) are facilitated as if the SUT can operate unrestricted. |


### Default credentials

#### `default_credential_A`

A Credential (EAA), in both 'mdoc' and 'SD-JWT VC' format. The Credential is issued by 'Issuer A'. It can be any type of Credential (mdoc 'doctype' or SD-JWT VC 'vct').

The Credential has at least the following attributes:
| Attribute | Type | Value |
| --- | --- | --- |
| `attribute_A` | numerical | positive number |
| `attribute_B` | string | non-empty string consisting of latin-1 characters, maximum of 64 characters. |
| `attribute_C` | date | a valid date in the past |

#### `default_credential_B`

*To be defined* TODO

The Credential has at least the following attributes:
| Attribute | Type | Value |
| --- | --- | --- |

#### `default_credential_C`

*To be defined* TODO

The Credential has at least the following attributes:
| Attribute | Type | Value |
| --- | --- | --- |

### Test - trust establishment
Tests are designed to be executed in a controlled environment. The FCAF assumes this environment is separate from production, with control over all facets.
A key reason to have a separate environment is to control which systems in the ecosystem can be trusted. Functional testing includes tests with explicitly trusted and non-trusted systems, as well as various unhappy flows (negative test cases), so control of trust relations is essential. This cannot be handled using production network trust infrastructure, as policies typically do not allow test systems that can produce intentionally incorrect data to be trusted.
Another reason to have a controlled environment is so no external changes can influence or disrupt testing.

In order to establish trust for tests (and explicit non-trust for unhappy flows or negative tests), a trusted list of trust lists and related certificate hierarchies will be detailed below. As with credentials, these are described logically or conceptually; it is up to testers and test tools to use specific instances of trust lists and certificates.
Specific tests rely on "trusted" lists or certificates. These tests assume trusted lists or certificates are loaded, available for the SUT to download, or otherwise configured. Managing and configuring the trust anchors for the SUT is out of scope of the FCAF.
