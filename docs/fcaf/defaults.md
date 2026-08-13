# Default items

The following sections define the SUT configurations, credentials, and trust anchors used throughout the test case specifications.
These definitions are intentionally logical rather than physical: they describe the required structures and characteristics, but not specific values. The tester or test tooling supplies concrete values for test execution.

## Default configurations

The following properties are defined for a SUT, specifically an EUDI Wallet Unit. The SUT is assumed to have these properties when the default configuration is used.

### `default_configuration_A`

| Property | Setting, contents, or value |
| --- | --- |
| App software | Installed on a mobile device. |
| App permissions | All relevant permissions are granted to the Wallet App in accordance with the Wallet Provider's instructions. |
| Peripherals and sensors | Any companion hardware is connected, and relevant sensors, such as NFC, BLE, or USB, are enabled, if applicable. |
| App personalisation | The App instance is personalised, has local authentication configured, and is registered with the Wallet Provider, if applicable. |
| WSCA/WSCD | The Wallet Unit's WSCA/WSCD is set up, linked to the Wallet Instance, and available for use. |
| App localisation | The App is configured to use a supported language. |
| EUDI Wallet state | Valid. In accordance with the EUDI Wallet specifications, the Wallet has a valid PID, is active, and has not been revoked. |
| Operating system and platform | The software of the underlying system, or test apparatus, is installed, configured, and ready for use. |
| Complementary software | Software such as a compliant browser, or user agent, is installed and ready for use. |
| Consent defaults | There is no preregistered consent for specific Relying Parties, Credentials, or Attributes. |
| Stored credentials | The Wallet Unit has been issued `default_credential_A`, `default_credential_B`, and `default_credential_C`, and these Credentials remain valid. |
| Network connectivity | Data connectivity is available and unrestricted. If filtering is applied for an isolated test network, all dependencies, such as DNS and NTP, are provided so that the SUT can operate without restriction. |

## Default credentials

### `default_credential_A`

A Credential, specifically an EAA, in both mdoc and SD-JWT VC format. The Credential is issued by `Issuer A`. It may be any type of Credential, identified by an mdoc `doctype` or an SD-JWT VC `vct`.

The Credential has at least the following Attributes:

| Attribute | Type | Value |
| --- | --- | --- |
| `attribute_A` | numerical | positive number |
| `attribute_B` | string | non-empty string consisting of Latin-1 characters, with a maximum length of 64 characters |
| `attribute_C` | date | valid date in the past |

### `default_credential_B`

*To be defined* TODO

The Credential has at least the following Attributes:

| Attribute | Type | Value |
| --- | --- | --- |

### `default_credential_C`

*To be defined* TODO

The Credential has at least the following Attributes:

| Attribute | Type | Value |
| --- | --- | --- |

## Test trust establishment

Tests are designed to run in a controlled environment. The FCAF assumes that this environment is separate from production and that all aspects of it can be controlled.
A separate environment is necessary to control which systems in the ecosystem are trusted. Functional testing includes tests with explicitly trusted and untrusted systems, as well as unsuccessful flows, or negative test cases, so control of trust relationships is essential. Production trust infrastructure cannot support this because its policies typically do not allow trust in test systems that intentionally produce incorrect data.
A controlled environment also prevents external changes from influencing or disrupting testing.

To establish trust for tests, and explicit non-trust for unsuccessful flows or negative tests, trusted lists, trust lists, and related certificate hierarchies will be described below. As with Credentials, these are described logically or conceptually. Testers and test tools must supply specific instances of trust lists and certificates.
Specific tests rely on trusted lists or certificates. Those tests assume that the lists or certificates are loaded, are available for the SUT to download, or are otherwise configured. Managing and configuring the SUT's trust anchors is outside the scope of the FCAF.
