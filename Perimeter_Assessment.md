# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 ([172.88.0.10]):** [http / Nginx 1.14.2]
* **Host 2 ([172.88.0.15]):** [No open ports detected]
* **Host 3 ([172.88.0.20]):** [http / Apache http 2.4.66 ((Unix))]

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** [Missing X-Frame-Options header]
* **Web Server 2 Finding:** [HTTP TRACE method enable vulnerable to XST attack]

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** [Outdated Nginx 1.14.2 web server on internet facing host 172.88.0.10]
* **Justification:** [Host 172.88.0.10 is top priority because the likehood of exploitation is high, Nginx 1.14.2 is an unpatched 2018 version with publicly known CVEs that attacters can easily exploit. The impact is critical as the missing X-Frame-Options header further exposes the server and its users, potentially resulting in full server compromise or clickjacking attacks.]
