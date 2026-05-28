# Week 1: Linux System Administration Essentials

## 📌 Overview
This repository contains production ready labs focusing on core Linux administration, system security, and text stream processing. The objective of this module was to transition from basic CLI navigation to managing enterprise level headless environments, auditing user permissions, and parsing high volume log data.

---

## 🛠️ Core Technical Proficiencies

* **Filesystem Architecture:** Deep understanding of the Filesystem Hierarchy Standard (FHS) to map complex, multi directory web applications and locate critical system configurations.
* **Access Control & System Security:** Mastery of the Read-Write-Execute (RWX) matrix utilizing both **Octal** and **Symbolic** notations. Experienced in managing special bits and remediating critical permission vulnerabilities.
* **Stream Editing & Log Interrogation:** Advanced data manipulation using standard streams (`stdin`, `stdout`, `stderr`) combined with `grep`, `sed`, and `awk` to parse, filter, and extract intelligence from massive datasets.

---

## 📂 Lab Breakdown & Architecture

### 📁 Session 01: The Shell Awakening
* **Objective:** Achieve 100% fluid navigation in headless Linux environments.
* **Practical Application:** Executed a configuration "Scavenger Hunt" to locate, map, and analyze multi directory web application structures and core system configuration files.

### 📁 Session 02: The Permissions Gauntlet
* **Objective:** Master user/group isolation and secure the filesystem matrix.
* **Practical Application:** Architected precise group-writable file boundaries and performed critical diagnostics to fix insecure permission errors within `/etc/shadow`.

### 📁 Session 03: Stream Editing & Piping
* **Objective:** Treat text as a data stream for automated transformation and security auditing.
* **Practical Application:** Developed a pipeline to strip raw Apache error logs into dedicated operational files and engineered a command-line string to isolate the top attacking IP addresses from a **10,000-line web server log**.

---

## 🚀 Key Commands & Tools Mastered
| Category | Tools / Concepts |
| :--- | :--- |
| **Navigation** | `cd`, `ls -la`, `tree`, `find`, `locate` |
| **Permissions** | `chmod` (Octal/Symbolic), `chown`, `chgrp`, SUID/SGID |
| **Text Processing** | `grep`, `sed`, `awk`, `cut`, `sort`, `uniq -c` |
| **I/O Redirection** | `>`, `>>`, `|`, `2>` |

---

## 📊 Key Artifacts
* `[Insert file path if you saved your top IPs output]`: Results of the 10,000 line Apache log analysis identifying threat vectors.
