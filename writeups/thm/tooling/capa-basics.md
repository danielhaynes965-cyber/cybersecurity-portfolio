# CAPA: The Basics

**Path:** Cyber Security 101 > Defensive Security Tooling  

**Date Completed:** Mar 08, 2026  

**Difficulty:** Easy

---

## Summary
This room introduces CAPA, an open-source tool by Mandiant used to identify capabilities in executable files. It provides a high-level overview of what a program *can* do (e.g., install a service, encrypt files, or communicate over HTTP) by mapping code patterns to known malware behaviors.

---

## Key Concepts
* **Static Analysis:** CAPA performs static analysis, meaning it identifies functionality without actually executing the potentially malicious file.
* **Rule-Based Detection:** It uses a collection of YAML-formatted rules to match assembly patterns, API calls, and strings against known behaviors.
* **Framework Mapping:** Results are automatically mapped to the **MITRE ATT&CK** framework and the **Malware Behavior Catalogue (MBC)** for standardized reporting.
* **Namespaces:** Rules are organized into hierarchical namespaces (e.g., `communication/http`, `anti-analysis/anti-vm`) to help analysts quickly categorize the threat.

---

## Commands & Tools
```bash
# Display help and all available CLI options
capa -h

# Perform a basic analysis on a suspicious binary
capa suspicious_file.exe

# Run with verbose output to see which rules matched (method level)
capa -v suspicious_file.exe

# Run with very verbose output to see exact assembly/locations of matches
capa -vv suspicious_file.exe

# Export results to JSON for use in the CAPA Web Explorer
capa -j suspicious_file.exe > results.json
```

___

## What I Learned
- CAPA identifies what a file is capable of doing, but the analyst must still determine if those capabilities are used for malicious intent.
- Using -vv is essential when you need to find the specific offset or function address where a behavior (like an anti-debugging check) occurs.
- Rules found in the nursery namespace are still in testing and may produce false positives or require manual verification.
- Exporting to JSON and using the Web Explorer makes analyzing complex binaries much easier than scrolling through a massive terminal output.

___

## References
- [Mandiant CAPA GitHub Repository](https://github.com/mandiant/capa)
- [CAPA Rules Documentation](https://github.com/mandiant/capa-rules)
- [Malware Behavior Catalogue (MBC)](https://www.google.com/search?q=https://github.com/MBCProject/bad-can)
