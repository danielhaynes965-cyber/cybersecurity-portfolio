# Nmap: The Basics

**Path:** Cyber Security 101 > Networking

**Date Completed:** January 7, 2026  

**Difficulty:** Easy  

---

## Summary
This room introduces Nmap as the industry-standard tool for network discovery and security auditing. It details various scanning techniques, from stealthy SYN scans to comprehensive service and OS detection.

---

## Key Concepts
* Nmap provides multiple scan types, including TCP connect scans (-sT) and stealthier SYN scans (-sS) that only perform the first step of the handshake.
* Port scanning can be customized to check all 65,535 ports (-p-) or focused on the top 100 most common ports (-F).
* Aggressive scanning (-A) combines OS detection, service versioning, and script scanning into a single command.
* Timing templates range from paranoid (0) to insane (5), allowing users to balance scan speed against the risk of detection or network congestion.
* Output can be saved in multiple formats, including grep-able (-oG) and XML (-oX), to facilitate further automation and reporting.

---

## Commands & Tools
```bash
# Execute a comprehensive scan with default scripts and service detection
nmap -sC -sV -p- -T4 --min-rate=9326 -vv [MACHINE_IP]

# Perform a quick host discovery ping scan without checking ports
nmap -sn [target]

# Run a stealth SYN scan on common ports
nmap -sS -F [target]

# Attempt to identify the operating system of the target
nmap -O [target]

# Output scan results in all major formats for reporting
nmap -oA [basename] [target]
```

---


```bash
-sL	# List scan – list targets without scanning

# Host Discovery	
-sn # Ping scan – host discovery only

# Port Scanning	
-sT # TCP connect scan – complete three-way handshake
-sS	# TCP SYN – only first step of the three-way handshake
-sU	# UDP Scan
-F # Fast mode – scans the 100 most common ports
-p[range] # Specifies a range of port numbers – -p- scans all the ports
-Pn	# Treat all hosts as online – scan hosts that appear to be down

# Service Detection	
-O # OS detection
-sV	# Service version detection
-A # OS detection, version detection, and other additions

# Timing	
-T <0-5> # Timing template – paranoid (0), sneaky (1), polite (2), normal (3), aggressive (4), and insane (5)
--min-parallelism <numprobes> and --max-parallelism <numprobes>	# Minimum and maximum number of parallel probes
--min-rate <number> and --max-rate <number> #	Minimum and maximum rate (packets/second)
--host-timeout # Maximum amount of time to wait for a target host

# Real-time output	
-v # Verbosity level – for example, -vv and -v4
-d # Debugging level – for example -d and -d9

# Reporting	
-oN <filename> # Normal output
-oX <filename> # XML output
-oG <filename> # grep-able output
-oA <basename> # Output in all major formats

```
---

## What I Learned
* The `-Pn` flag is critical when scanning hosts that block ICMP requests, as it tells Nmap to treat the host as online.
* Using `-sV` is essential for identifying specific service versions, which helps in finding associated CVEs and exploits.
* Setting a specific `--min-rate` ensures the scan proceeds at a constant speed, which is useful for large-scale network discovery.
* High verbosity (`-vv`) provides real-time feedback on open ports as they are discovered, rather than waiting for the scan to finish.
* Default script scanning (`-sC`) automates common tasks like checking for open shares or basic vulnerabilities on detected services.

---

## References
- [Nmap Official Documentation](https://nmap.org/book/man.html)
