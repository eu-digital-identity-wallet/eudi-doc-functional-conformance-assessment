# EuPid_DM_BirthPlace_05

## Objective
This test case verifies that the country item of data element birth_place is a valid country code.

## References
European Digital Identity Wallet, ARF 2.0, Annex 3.01 pid rulebook, paragraph 3.1.5  
 ISO/IEC 3166-1

## EUDI-wallet relevancy
EUDI_specific | EUDI_required

## Profile applicability
The mdoc contains a document with DocType = "eu.europa.ec.eudi.pid.1".

## Preconditions
A. A device retrieval mdoc request was sent to the EUDI wallet, to retrieve the document with DocType = "eu.europa.ec.eudi.pid.1". 
B. All mandatory data elements within nameSpace "eu.europa.ec.eudi.pid.1" and all data elements indicated as present in the ICS were requested. 
C. The device retrieval mdoc response was retrieved. 
D. The presence of the item ‘country’ in data element birth_place in the device retrieval mdoc response was verified.

## Test Scenario
1. Verify that the value of the data element `country` in map place_of_birth contains a valid country code.

## Expected results
1. The DataElementValue has two characters, an alpha-2 code, corresponding to a country name: Listed in ISO 3166-1:2020, 6.1. Not listed in ISO 3166-1:2020, 6.1. In this case, the user-assigned country codes may be used, which consist in the series of letters AA, QM to QZ, XA to XZ, and ZZ (ISO 3166-1:2020, 8.3).

## 
