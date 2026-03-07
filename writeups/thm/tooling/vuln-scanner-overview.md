# Vulnerability Scanner Overview

**Path:** Cyber Security 101 > Security Solutions  

**Date Completed:** Feb 28, 2026  

**Difficulty:** Easy

---

## Summary
This room serves as a foundational look at the automated discovery of security weaknesses. It explains how scanners identify, prioritize, and help remediate vulnerabilities by comparing system attributes against massive databases of known flaws like CVEs.

---

## Key Concepts
### **1. Scanning Mechanisms**
* **Mechanism:** Scanners perform "fingerprinting" by checking banners, version numbers, and open ports against a library of known vulnerabilities.
* **The Goal:** Proactive defense—identifying the "holes" before a threat actor can exploit them.

### **2. Scan Depth & Methodology**
* **Depth:**
    * **Authenticated (Internal):** Uses credentials to inspect registry keys and local patches; high accuracy.
    * **Unauthenticated (External):** Probes from the outside; limited to network-facing services.
* **Methodology:**
    * **Active:** Sends packets directly to targets; thorough but can be noisy or disruptive.
    * **Passive:** Listens to existing network traffic; stealthy but provides less detail.

### **3. Scoring & Prioritization**
* **CVSS (Common Vulnerability Scoring System):** A static 0-10 numerical score indicating severity.
* **VPR (Vulnerability Priority Rating):** A dynamic score that fluctuates based on the current real-world threat landscape.



### **4. Vulnerability Management Lifecycle**
1. **Identification:** Discovering all assets on the network.
2. **Prioritization:** Ranking flaws based on risk (CVSS/VPR).
3. **Remediation:** Patching, updating, or reconfiguring.
4. **Verification:** Rescanning to ensure the fix was successful.



---

## Commands & Tools
```bash
# --- Nikto (Web Specialized Scanner) ---
# Scan a specific web server for dangerous files/outdated software
nikto -h http://10.10.10.10

# --- OpenVAS / Nessus (General Purpose) ---
# These are primarily GUI-based tools. 
# Key Workflow: Create Policy -> Define Target (Scope) -> Launch Scan -> Analyze Report

# --- CVSS Scoring Logic ---
# Base Score is determined by:
# f(Impact, Exploitability) 
# Where:
# Impact = Confidentiality, Integrity, Availability
# Exploitability = Attack Vector, Complexity, Privileges Required
```

## What I Learned
- While CVSS tells you how "bad" a bug is, VPR tells you if anyone is actually exploiting it right now, which is far more critical for real-world prioritization.
- Scanners are not magic; they generally cannot find vulnerabilities that aren't already in their database (False Negatives), making manual testing still necessary.
- The lifecycle doesn't end at patching; you must always perform a follow-up scan to verify that the remediation was actually successful and didn't introduce new issues.
