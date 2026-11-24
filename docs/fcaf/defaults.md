# Default items

The following sections define the SUT configurations, credentials, and trust anchors used throughout the test case specifications.
These definitions are intentionally logical rather than physical: they describe the required structures and characteristics, but not specific values. The tester or test tooling supplies concrete values for test execution.

## Default configurations

The following properties are defined for a SUT, specifically an EUDI Wallet Unit. The SUT is assumed to have these properties when the default configuration is used.

### `default_configuration_1`

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

Unless a test case states a deviation, the SD-JWT VC variant of every default credential carries the issuer's signing certificate and its chain, excluding the trust anchor, in the `x5c` header parameter ([HAIP] clause 6.1.1, applied through [CIR 2024/2982 amended] Annex II OIDFVP-HAIP-GEN-05); where the Credential is a QEAA or a PuB-EAA, the protected header also carries `x5u` and `x5t#S256` ([ETSI TS 119 472-1] QEAA-5.6.2-02 and PuB-EAA-5.6.3-02). The mdoc variant carries the MSO signing certificate in the `x5chain` element of the `IssuerAuth` header ([ISO/IEC 18013-5]). A Credential that deviates from this is a named default item (`default_credential_F`), never an unnamed variation in a test step.

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

### `default_credential_E`

A Credential, specifically an EAA, in SD-JWT VC format only, issued by `Issuer A`, for test cases of SD-JWT VC Type Metadata. Its `vct` claim is an HTTPS URL under the tester's control that serves `default_type_metadata_A`, and it carries a `vct#integrity` claim matching that document. It has the Attributes of `default_credential_A`.

### `default_credential_F`

The SD-JWT VC variant of `default_credential_A`, issued by `Issuer A`, whose protected header carries no `x5c`, `x5u` or `x5t#S256` parameter; the Issuer's public key is published only through `default_jwt_vc_issuer_metadata_A`. It is not an EUDI-conformant PID or EAA ([HAIP] clause 6.1.1) and serves only the test cases of the JWT VC Issuer Metadata issuer signature mechanism ([SD-JWT VC] sections 3.5 and 5), whose relevancy is `EUDI_generic | EUDI_undefined`.

## Test trust establishment

Tests are designed to run in a controlled environment. The FCAF assumes that this environment is separate from production and that all aspects of it can be controlled.
A separate environment is necessary to control which systems in the ecosystem are trusted. Functional testing includes tests with explicitly trusted and untrusted systems, as well as unsuccessful flows, or negative test cases, so control of trust relationships is essential. Production trust infrastructure cannot support this because its policies typically do not allow trust in test systems that intentionally produce incorrect data.
A controlled environment also prevents external changes from influencing or disrupting testing.

To establish trust for tests, and explicit non-trust for unsuccessful flows or negative tests, trusted lists, trust lists, and related certificate hierarchies will be described below. As with Credentials, these are described logically or conceptually. Testers and test tools must supply specific instances of trust lists and certificates.
Specific tests rely on trusted lists or certificates. Those tests assume that the lists or certificates are loaded, are available for the SUT to download, or are otherwise configured. Managing and configuring the SUT's trust anchors is outside the scope of the FCAF.

## Default metadata documents

The documents below are served by the test apparatus with HTTP status `200` and content type `application/json`; [SD-JWT VC] section 6.3.1 itself requires only that the response to the GET is a JSON object as defined in its section 6.2. As with Credentials, they are described logically; the tester supplies the URLs and values.

### `default_type_metadata_A`

The SD-JWT VC Type Metadata document of `default_credential_E`, served at the `vct` URL of that Credential.

| Member | Value |
| --- | --- |
| `vct` | identical to the `vct` claim of `default_credential_E` |
| `display` | an array with one object: `locale` a supported language tag, `name` a non-empty string |
| `claims` | an array with one object per Attribute of `default_credential_E`: `path` addressing the Attribute, `display` with `locale` and `label` |

### `default_type_metadata_B`

An SD-JWT VC Type Metadata document that extends `default_type_metadata_A`, served at its own HTTPS URL under the tester's control. A `default_credential_E` of this type carries that URL in its `vct` claim and a matching `vct#integrity` claim.

| Member | Value |
| --- | --- |
| `vct` | the URL at which this document is served |
| `extends` | the `vct` of `default_type_metadata_A` |
| `extends#integrity` | the integrity metadata of `default_type_metadata_A` |

### `default_type_metadata_C`

As `default_type_metadata_B`, but extending `default_type_metadata_B`: its `extends` is the `vct` of `default_type_metadata_B` and its `extends#integrity` the integrity metadata of that document.

### `default_jwt_vc_issuer_metadata_A`

The JWT VC Issuer Metadata configuration of `Issuer A`, served at the location formed by inserting `/.well-known/jwt-vc-issuer` between the host component and the path component of the `iss` claim of Issuer A's SD-JWT VCs. `default_credential_F` relies on it.

| Member | Value |
| --- | --- |
| `issuer` | identical to the `iss` claim of the SD-JWT VC |
| `jwks` | a JWK Set containing the public key that verifies Issuer A's signature, with a `kid` |

### `default_jwt_vc_issuer_metadata_B`

A variant of `default_jwt_vc_issuer_metadata_A` for test cases in which the Issuer publishes its key by reference. Where a test case names it, `Issuer A` serves it at the same location in place of `default_jwt_vc_issuer_metadata_A`. It carries no `jwks` member.

| Member | Value |
| --- | --- |
| `issuer` | identical to the `iss` claim of the SD-JWT VC |
| `jwks_uri` | an HTTPS URL under the tester's control that serves a JWK Set containing the public key that verifies Issuer A's signature, with a `kid` |
