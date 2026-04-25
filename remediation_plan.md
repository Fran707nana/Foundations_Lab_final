# CLOUDNANO REMEDIATION PLAN
**Operator:** Franklin G
 TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **[Unauthenticated AWS S3 Bucket (Contains Customer PII)]**
   * **Justification:** [The reason why this vulnerability is top 1 is because there is no need for any special tool or skills since the bucket is already open, customer PII are fully exposed and one can view them.]

2. **[SQL Injection in Login Page (Customer Database Portal)]**
   * **Justification:** [The reason why this vulnerability is #2 is because an attacker can bypass authentication requirements entirely without the need of a password. Once inside the attacker can access the customer database, they can steal customer PII and do whatever they like with it.]

3. **[Remote Code Execution in Apache Struts (Internet Facing Web Server)]**
   * **Justification:** [The reason why this vulnerability is #3 is because the server is internet facing meaning any one can see it. If an attacker gains control over the serve they can literally steal, share or take the server as a hostage and ask for money. ]

4. **[Outdated PHP Version 5.4 (Public Marketing Blog)]**
   * **Justification:** [The reason why this vulnerability is #4 because public facing makes it likely exploitable. Even though it hasn't such big impact as the other top 3, the public logs can still be used as a point to spread malware if an attacker take control over and decides to do that. ]

5. **[Cross-Site Scripting (XSS) on Support Forum]**
   * **Justification:** [The reason why this vulnerability is at last place is because even though an attacker can still user credentials and see their PII  the attacker can only steal one user at a time, meaning they can still cause harm but a low level compared to the other scenarios.]

