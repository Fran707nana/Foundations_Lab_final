# Week 4: Fortifying the Node (Infrastructure Hardening)

### 📌 Overview

This repository documents a transition from a security tool builder to an infrastructure hardening architect. This module focused on establishing defensive perimeters, microsegmentation, and zero-trust isolation across modern virtualized deployments. The core focus was moving away from manual, single container imperative commands and transforming exposed, default configured software systems into locked down, monitored, and segmented enterprise infrastructure engineered to withstand targeted exploitation.

### 🛠️ Core Technical Proficiencies Mastered

* **Hypervisor Architecture & Malware Isolation:** Developed functional competency in mapping structural differences between Type 1 (Bare Metal) and Type 2 (Hosted) virtualization layers to build air gapped sandboxes where executing threat vectors cannot escape to the local production network.
* **OS-Level Namespace Isolation:** Mastered container virtualization mechanics over standard hardware virtualization, using lightweight Linux namespaces to provision, interact with, and completely destroy ephemeral web nodes with zero permanent system footprints.
* **Declarative Stack Orchestration:** Transitioned from imperative command line executions to writing declarative, version controlled multi container configurations using YAML arrays within Docker Compose environments.
* **Zero-Trust Network Microsegmentation:** Engineered segmented network boundaries by constructing distinct front facing communication paths and completely air gapping backend datastores utilizing strict `internal: true` networking layers.

---

### 📂 Automated Infrastructure Portfolio

#### 📁 Session 10: The Ghost in the Machine (Virtualization & Hypervisors)
* **Objective:** Map structural hypervisor topologies and master software defined virtual networking to contain threat actors.
* **Practical Application (Operation Sandbox Isolation):** Migrated an active VirtualBox VM profile from a public-facing `Bridged` adapter topology down to an isolated `Host-Only` layout, executed a provisioning script to seed a simulated malware payload within a designated Quarantine Zone, and documented forensic connection metrics.
* **Core Artifact:** `sandbox_report.txt`

#### 📁 Session 11: The Container Revolution (Docker Fundamentals)
* **Objective:** Contrast structural hardware level virtualization against lightweight OS-level kernel namespace sharing.
* **Practical Application (Operation Rapid Deployment):** Programmatically provisioned minimalist Alpine distributions, audited systemic namespace boundaries using native `ps aux` process accounting flags, and engineered a script to automate the rapid deployment, content modification, log auditing, and zero-footprint teardown of a live Nginx node.
* **Core Artifact:** `deploy_web.sh`

#### 📁 Session 12: The Conductor and the Fleet (Docker Compose & Orchestration)
* **Objective:** Move from single container imperative commands to declarative multi container orchestration using YAML configuration models.
* **Practical Application (Operation Segmented Stack):** Hand drafted custom multi container blueprints to deploy a mutually dependent WordPress and MySQL stack. Mapped public traffic safely to a front facing network segment while programmatically locking down database states inside an air gapped network with zero external internet routing.
* **Core Artifact:** `docker-compose.yml`

---

### 🛡️ Capstone Integration: Operation Fortified Node (Week 4 TLAB)

* **Role:** Security Infrastructure Engineer
* **Objective:** Deploy a segmented three tier containerized stack and a legacy VM sandbox in a hardened, isolated hybrid architecture while auditing network perimeters to verify the zero trust boundary.
* **Environment Sanitation:** Audited the active host network socket matrix to detect conflicting legacy configurations, successfully executing an environment eviction of an unauthorized squatter container (`decoy_web`) to clear Port 80.
* **Declarative Architecture Engineering:** Wrote a production ready `docker-compose.yml` blueprint from scratch to instantiate two distinct networks (`public_net` and an `internal: true` private net), a persistent database storage volume (`db_data`), and tied them to integrated MariaDB and WordPress containers.
* **Perimeter Isolation Auditing:** Conducted network interface discovery (`ip addr`) and targeted network mapper (`nmap`) sweeps to verify that port 80 remained open to authorized public traffic while database port 3306 was completely masked from external networks.
* **Air-Gap Verification:** Crossed into the live runtime web container namespace to attempt direct packet forwarding out to the host-managed `Host-Only` legacy VM sandbox, validating and logging a verified routing failure.
* **Machine-Readable Telemetry Export:** Structured environmental metrics, interface IPs, and container isolation validation results into a fully verified, enterprise ready JSON alert artifact.
* **Core Artifacts:** `docker-compose.yml` | `hyperstack_audit.json`

---

### 🚀 Technical Implementation Matrix

| Tool/Script / Artifact | Engineering Mechanics Highlighted | Core Systems/Engines Used |
| :--- | :--- | :--- |
| **`sandbox_report.txt`** | Hypervisor boundary configuration, Host-Only networking, malware detonation forensics | VirtualBox, Linux Kernel |
| **`deploy_web.sh`** | Ephemeral infrastructure provisioning, OS-level namespace auditing, zero footprint automation | Docker Engine, Bash CLI, Alpine Linux |
| **`docker-compose.yml`** | Declarative orchestration, YAML array engineering, internal network microsegmentation | Docker Compose, WordPress, MariaDB |
| **`hyperstack_audit.json`** | Multi tiered validation reporting, machine readable telemetry parsing, persistence verification | JSON Serialization, Nmap Routing Audit |
