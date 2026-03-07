# Metasploit Framework (Intro, Exploitation, & Meterpreter)

**Path:** Cyber Security 101 > Exploitation Basics  

**Date Completed:** Jan 2026  

**Difficulty:** Medium

---

## Summary
This writeup covers the complete Metasploit lifecycle, from fundamental architecture and database enumeration to advanced exploitation and post-exploitation. It highlights the importance of managing workspaces, understanding payload differences, and leveraging Meterpreter for stealthy, in-memory command and control.

---

## Key Concepts
* **Core Architecture:** Metasploit utilizes specific modules for the entire kill chain, including exploits, payloads, auxiliary tools, post-exploitation scripts, and evasion tactics.
* **Metasploit Database (msfdb):** Automates the tracking of hosts, services, and vulnerabilities. Using workspaces keeps separate CTF targets organized.
* **Payload Types (Staged vs. Inline):** * *Staged (`/`):* Sends a small stager to pull a larger payload, ideal for limited buffer space.
    * *Inline (`_`):* Sends the entire payload at once, which is often more stable against strict firewalls.
* **Meterpreter:** An advanced C2 payload that operates stealthily entirely in memory via Reflective DLL Injection. It uses TLS/SSL encrypted communication to evade IDS/IPS detection.

---

## Commands & Tools

### msfconsole Navigation & Configuration
```bash
# Navigation
help / ?                    # Displays available commands
search [keyword]            # Finds modules related to a service or CVE
use [index/path]            # Selects a module
info                        # Detailed module info: CVE, options, and targets
show [options/payloads]     # Displays configurations for the current module
back                        # Moves out of the current module context

# Configuration & Execution
set [variable] [value]      # Assigns a value to a local variable (e.g. RHOSTS)
setg [variable] [value]     # Sets a global variable for all modules
unset / unsetg              # Clears local or global variables
exploit / run               # Launches the module
check                       # Tests vulnerability without exploiting
```

### Database Management (msfdb)
```bash
msfdb init                  # Initializes the PostgreSQL database from terminal
db_status                   # Verifies database connection
workspace -a [name]         # Creates/switches project environments
db_nmap [options]           # Runs Nmap and saves results to DB
hosts                       # Lists discovered IP addresses
services                    # Lists discovered ports and services
vulns                       # Lists identified vulnerabilities
```

### Meterpreter & Post Exploitation
```bash
# Session Management
background / bg             # Backgrounds current session
sessions -i [ID]            # Interacts with a backgrounded session
sessions -u [ID]            # Upgrades a basic shell to Meterpreter

# System Operations
sysinfo / getuid            # Identifies OS architecture and user context
ps                          # Lists running processes
migrate [PID]               # Moves process for stability/stealth
getsystem                   # Attempts elevation to SYSTEM (Windows)
hashdump                    # Dumps NTLM hashes from SAM database

# File System & Networking
search -f [file]            # Searches for specific files
upload / download           # Transfers files between host and target
checksum md5 [file]         # Verifies file integrity
ipconfig / route            # Identifies network interfaces and routing
portfwd add -l 3389 -r [IP] # Forwards remote ports for pivoting

# Post-Exploitation Modules
run post/multi/recon/local_exploit_suggester # Finds PrivEsc paths
run post/windows/gather/checkvm              # Checks if target is a VM
```
---

## What I Learned
* As soon as a session is established, use `ps` to find a stable process (like `explorer.exe` for users or `services.exe` for system) and `migrate [PID]` to ensure the shell survives if the initial exploited application or web server crashes.
* Running `post/multi/recon/local_exploit_suggester` should be a default step if you aren't already SYSTEM; it automates the search for local vulnerabilities and saves hours of manual research.
* The distinction between staged (`/`) and inline (`_`) payloads is a critical technical detail; inline payloads are generally more stable and better for bypassing firewalls that block the second "stage" download.
* If an exploit only provides a basic command shell, backgrounding it with `Ctrl+Z` and using `sessions -u [ID]` is the most efficient way to access the full Meterpreter toolkit.
* Using `msfdb` and `workspaces` is essential for CTFs to automate the tracking of services and vulnerabilities, preventing the loss of reconnaissance data across long sessions.
* For professional practice (and stealth), use `clearev` to wipe Application, System, and Security logs on Windows targets before exiting the system.
