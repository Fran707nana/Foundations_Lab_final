# Week 3: Scripting the Defense (Security Automation)

## 📌 Overview
This repository documents a transition from a security operator to a security tool builder. This module focused on leveraging Python as a defensive instrument and force multiplier for Security Operations Center (SOC) environments. The core focus was translating manual, one time command line operations into automated, repeatable, and scalable security tools engineered for production stability.

---

## 🛠️ Core Technical Proficiencies Mastered

* **Defensive Script Engineering:** Developed functional, automated scripts utilizing core low-level libraries like `socket`, `subprocess`, and `os` to audit network vectors and interface with the host operating system.
* **Production-Grade Architecture:** Mitigated risk to production by utilizing Python Virtual Environments (`venv`) to completely isolate scripts from the host OS dependencies, and implemented strict variable casting to prevent script killing `TypeErrors`.
* **High-Volume Data Processing:** Mastered the utilization of programmatic control flows (`for` loops and `if/else` conditional matrices) combined with native Python data structures (`Lists`, membership operators) to parse massive datasets without manual intervention.
* **Resilient Error Handling & Data Serialization:** Built "graceful failure" exceptions into defensive scripting utilizing `try/except` blocks, and exported high fidelity threat telemetry into structured `JSON` formats for ingestion by SIEM platforms.

---

## 📂 Automated Security Tool Portfolio

### 📁 Session 07: The Sentry (Python Foundations)
* **Objective:** Master input handling, strict type safety, and environment isolation.
* **Practical Application (*Operation Port Scan*):** Stabilized script input variables using explicit string to integer mathematical casting to prevent logic failures, and fully isolated the script execution workspace within a virtual environment.
* **Core Artifact:** `port_check.py`

### 📁 Session 08: The Paper Trail (Logic, Loops, & Lists)
* **Objective:** Architect autonomous decision making logic over high volume data arrays.
* **Practical Application (*Operation Logical Filter*):** Engineered a real time tracking mechanism that uses Python membership operators (`in`) to evaluate live network traffic against a database array of known malicious IPs, automatically flagging risk vectors based on severity.
* **Core Artifact:** `log_filter.py`

### 📁 Session 09: The Conductor (Functional Automation)
* **Objective:** Encapsulate logic into reusable functions and automate system level file manipulation.
* **Practical Application (*Operation Scripted Firewall*):** Constructed a functional automation bot that opens raw `access.log` text pools programmatically, scans the stream for `"FAILED"` authentication signatures, and dynamically appends the flagged vectors to an actionable blocklist file.
* **Core Artifact:** `firewall_bot.py`

---

## 🛡️ Capstone Integration: Operation Automated Hunt (Week 3 TLAB)
**Role:** Security Automation Engineer  
**Objective:** Synthesize Stream Parsing, File I/O, and Subprocess monitoring into an automated incident response script designed to mitigate a simulated live brute force attack.

* **Log Interrogation:** Leveraged Python's `subprocess` module to programmatically execute kernel level string filtering against native Linux security logs (`auth_sim.log`).
* **Data Parsing:** Developed parsing logic to break down raw unstructured text blocks, loop through live authentication strings, isolate specific space delimited indexes, and aggregate unique attacker IP strings into processing arrays.
* **Threat Intel Export:** Automated the transformation of raw lists into a validated Python dictionary, serializing the structured threat telemetry into an enterprise ready JSON alert artifact.
* **Core Artifacts:** `incident_response.py` | `threat_report.json`

---

## 🚀 Technical Implementation Matrix
| Tool/Script | Engineering Mechanics Highlighted | Core Libraries Used |
| :--- | :--- | :--- |
| **`port_check.py`** | Input data sanitization, variable casting, type safety validation | `socket`, `sys` |
| **`log_filter.py`** | Iterative processing arrays, conditional branching matrices, list comparison | Native Python |
| **`firewall_bot.py`** | Robust `try/except` exception tracking, programmatic File I/O stream reading/writing | `os` |
| **`incident_response.py`** | Core stream manipulation, system kernel subprocess execution, JSON serialization | `subprocess`, `json` |
