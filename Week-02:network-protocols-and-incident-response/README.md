# Week 2: Network Protocols and Incident Response

## 📌 Overview
This repository contains advanced labs focused on the OSI model, network boundary security, application layer protocols, and defensive incident response operations. The core objective of this module was to transition from passive network observation to active infrastructure troubleshooting, network segmentation, and live threat mitigation.

---

## 🛠️ Core Technical Proficiencies

* **OSI Layer 1-3 Diagnostics:** Proficient in using low level network utilities to map hardware addresses, audit physical interfaces, and manually rebuild routing paths in "blind" terminal environments.
* **Network Segmentation & CIDR Mathematics:** Deep understanding of IP addressing, CIDR notation, and binary octet manipulation. Capable of designing and troubleshooting secure network boundaries to prevent unauthorized cross-subnet communication.
* **Application Layer Auditing & Service Discovery:** Experienced in auditing active sockets, identifying non standard service ports, and remediating local network manipulation (such as DNS poisoning).

---

## 📂 Lab Breakdown & Incident Briefs

### 📁 Session 04: The Wire (L1-L3)
* **Objective:** Restore network connectivity to an isolated host via layer 1-3 diagnostics.
* **Practical Application (*Operation Broken Link*):** Interrogated physical interfaces using `ip link` and `ip addr`, identified hardware (MAC) addresses, and manually reconstructed a dropped default gateway.
* **Artifact Generated:** `network_audit.txt`

### 📁 Session 05: The Subnetting Crucible
* **Objective:** Master CIDR boundaries and network masking logic.
* **Practical Application (*Operation Grid Lock*):** Engineered a Python script to perform binary surgery on IP octets, visualizing subnet masks at the bitwise level. Successfully resolved a mathematical CIDR mismatch isolating a production host.
* **Artifact Generated:** `subnet_blueprint.txt`

### 📁 Session 06: Protocol Interrogation
* **Objective:** Audit open network vectors and remediate localized deceptive configurations.
* **Practical Application (*Operation Hidden Door*):** Utilized `ss` and `dig` to map active service sockets, discovered a web service hidden on a non standard port, and neutralized a poisoned `/etc/hosts` file.
* **Artifact Generated:** `protocol_audit.txt`

---

## 🛡️ Capstone Mission: Operation Silent Ghost (Take-Home Lab)
**Role:** SOC Analyst (Incident Response)  
**Mission Objective:** Respond to an active enterprise server compromise by synthesizing all network security controls mastered throughout the week.

* **Phase 1 (Re-establishment):** Diagnosed and brought up a downed network interface to restore communication with the compromised host.
* **Phase 2 (Segmentation):** Reconfigured an erroneous subnet mask to allow secure, authenticated traffic to reach the backend database.
* **Phase 3 (Exfiltration Detection):** Traced and intercepted network traffic on a hidden exfiltration port, capturing raw malicious packet headers to prevent data loss.

---

## 🚀 Toolbelt Matrix
| Utility | Use Case |
| :--- | :--- |
| `ip link / ip addr` | Interface state auditing and MAC configuration |
| `ss` | Socket statistics, active connection monitoring, and port auditing |
| `dig` | Domain Information Groper for DNS infrastructure queries |
| `Python` | Automated decimal-to-binary IP string conversions |
| `/etc/hosts` | Static local name resolution management and security auditing |
