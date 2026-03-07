# Hydra

**Path:** Cyber Security 101 > Offensive Security Tooling  

**Date Completed:** Jan 25, 2026  

**Difficulty:** Easy

---

## Summary
Hydra is a high-speed, parallelized network login cracker supporting numerous protocols including SSH, FTP, and HTTP. It is the industry-standard tool for online password attacks, allowing researchers to test credential validity against active services in real-time.

---

## Key Concepts
* Hydra is designed for speed, using multiple threads to attempt logins simultaneously.
* It can target almost any service that requires a handshake or login, from legacy FTP to modern Web Forms.

---

## Commands & Tools

### Essential Flags
* `-l <user>` / `-L <file>`: Target a specific username or a list of users.
* `-p <pass>` / `-P <file>`: Target a specific password or a wordlist (e.g., `rockyou.txt`).
* `-t <threads>`: Set speed (Default: 16). Lower this to avoid crashing services.
* `-v` / `-V`: Enable verbose mode to debug failed attempts.
* `-s <port>`: Specify a non-default service port.

### Common Service Examples
```bash
# SSH Brute-force
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.10.6 ssh

# FTP Brute-force
hydra -l admin -P passwords.txt 10.10.10.6 ftp

# Web Login Form (HTTP-POST-FORM)
# Structure: "Page:Body:Error_Message"
hydra -l admin -P rockyou.txt 10.10.10.6 http-post-form "/login.php:user=^USER^&pass=^PASS^:F=Invalid Username"
```

---

## What I Learned

- If Hydra marks every attempt as a success, the error message (F=...) is likely incorrect. Hydra assumes success by default if it doesn't see that specific failure string on the response page.
- While speed is a priority, high thread counts (-t 64+) often trigger account lockouts or cause service denial-of-service. Dropping to -t 4 is a common fix for unstable connections.
- For web forms, you must use the browser's Network Tab to capture the exact POST parameters (e.g., user=^USER^&pass=^PASS^) to ensure Hydra is communicating correctly with the backend.
- Never fire Hydra blindly; always verify the service and port with nmap -sV first to ensure you aren't wasting time on a filtered or non-existent service.

## References
- [SecLists](https://github.com/danielmiessler/SecLists)
