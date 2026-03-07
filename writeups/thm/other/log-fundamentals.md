# Logs Fundamentals

**Path:** Cyber Security 101 > Defensive Security  

**Date Completed:** Feb 26, 2026  

**Difficulty:** Easy

---

## Summary
This room covers the critical role of logging as the "digital footprint" of system activity. It focuses on how to categorize, locate, and analyze logs across Windows and Linux environments to reconstruct attack timelines or troubleshoot exploit failures.

---

## Key Concepts
* Logs are used for Detection (identifying the breach), Forensics (reconstructing the timeline), and Troubleshooting (fixing failed exploits).
* **Log Hierarchies:**
    * **Security:** Authentication and authorization (logins/permissions).
    * **System:** OS-level events (drivers/services).
    * **Network:** Traffic flow and data exfiltration.
    * **Access/Application:** Resource usage and specific software errors.
    * **Windows Event Logs:** Categorized into Application, System, and Security; filtered primarily by specific **Event IDs**.
    * **Web Logs:** Record the "Who, When, and What" of web requests (IP, Timestamp, Method, URL, Status Code).

---

## Commands & Tools
```bash
# --- Linux Log Parsing ---
# Search for a specific attacker IP in auth logs
grep "10.10.15.20" /var/log/auth.log

# Count unique IP addresses hitting a web server
awk '{print $1}' access.log | sort | uniq -c | sort -nr

# --- Windows Log Analysis (PowerShell) ---
# Filter Security logs for failed login attempts (Event ID 4625)
Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4625}

# List the last 5 system errors via CLI
wevtutil qe System /c:5 /f:text /q:"*[System[(Level=2)]]"
```

---

## What I Learned
- Memorizing common IDs (e.g., 4624 for successful login, 4625 for failure) is faster than scrolling through GUI menus during a timed CTF.
- A sudden spike in 404 Not Found errors in web logs is a dead giveaway for directory brute-forcing tools like Gobuster or Dirbuster.
- When parsing large logs with grep or awk, piping output to head or tail prevents terminal overflow.
- From an offensive perspective, the "Final Phase" of an engagement involves clearing or selectively editing these logs to remain undetected.
- /var/log/ is the central hub for Linux, while Windows relies on the proprietary .evtx format and the Event Viewer.
