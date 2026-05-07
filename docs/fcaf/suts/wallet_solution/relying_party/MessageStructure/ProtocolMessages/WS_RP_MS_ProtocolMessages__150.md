# WS_RP_MS_ProtocolMessages_150

## Objective
Test the wallet returns the error message vp_formats_not_supported when the wallet does not support any of the formats requested.
(vc+sd-jwt case)

## References
[OID4VP Section 8]

## Profile applicability


## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions
The wallet supports mso_mdoc, but does NOT support vc+sd-jwt

## Test Scenario
1. The wallet engages with verifier.
2. The verifier sends an Authorization request for format vc+sd-jwt.
3. Wallet processes request.
4. Test the response returned by the wallet to the Verifier.

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. The Wallet identifies it cannot fulfill request due to format requirement and does NOT show credential selection screen.
4. Verify the Wallet returns an error response, where the error parameter is exactly vp_formats_not_supported.

