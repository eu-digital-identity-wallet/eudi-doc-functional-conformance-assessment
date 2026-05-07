# WS_RP_IA_MainInteraction_059

## Objective
Test the Wallet redirects the user agent to the redirect_uri if this parameter is included in the Authorization Request.
Cross device DC API

## References
[OID4VP Section 8]

## Profile applicability
Cross device DC API

## EUDI-wallet relevancy
EUDI_generic | EUDI_required

## Preconditions


## Test Scenario
1. The wallet engages with the verifier
2. The verifier sends an Authorization request, with response_type=vp_token, and parameter redirect_uri
3. The wallet processes the request
4. The wallet constructs the URL

## Expected results
1. Wallet-verifier interaction is successfully initiated
2. Wallet receives request
3. True
4. Verify the wallet appends the Authorization response to the redirect_uri, opens URL in the browser

