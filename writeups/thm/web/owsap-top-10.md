# OWASP Top 10 (2025)

**Path:** Cyber Security 101 > OWASP Top 10 (2025)  

**Date Completed:** Mar 10, 2026  

**Difficulty:** Easy

---

## Summary
These rooms (as this is one writeup for a module of 3) teach how to explore, exploit, and remediate the most critical web application security risks listed in the OWASP Top 10 (2025) list through interactive labs and practical recommendations

---

## Key Concepts
- The OWASP Top 10 list summarises the most common and impactful vulnerabilities found within web applications

### A01 Broken Access Control

- When the server doesn't properly enforce IAAA (who can do what), e.g. IDOR (Insecure Direct Object Reference)
- In practice, this shows up as privilege escalation, either horizontal (same role, other user's stuff), or vertical (jumping to admin only actions)

### A02 Security Misconfigurations

- When systems, services, or application are deployed with unsafe defaults, incomplete settings, or exposed services.
- These aren't code bugs but mistakes in how the environment, software, or network is set up.
- They create easy entry points for attackers

### A03  Software Supply Chain Failures

- When applications rely on components, libraries, services, or models that are compromised, outdated, or improperly verified
- One compromised dependency can compromise your entire system, allowing attackers to gain access without ever touching your own code

### A04 Cryptographic Failures

- When encryption is used incorrectly or not at all (e.g. weak algorithms, hard-coded keys, poor key handling, or unencrypted sensitive data)

### A05 Injection

- When an application takes user input and mishandles it
- Instead of processing the input securely, the application passes it directly into a system that can execute commands or queries, such as a database, a shell, a templating engine or API

### A06 Insecure Design
- When flawed logic or architecture is built into a system from the start
- AI systems exacerbate insecure design


### A07 Authentication Failures

- When an application can't reliably verify or bind a user's identity due to poor authentication (e.g. username enumeration, weak/guessable passwords, etc)

### A08 Software or Data Integrity Failures

- When an application relies on code, updates, or data it assumes are safe, without verifying their authenticity, integrity, or origin

### A09 Logging & Alerting Failures

- When applications don't record or alert on security relavant events, making defenders unable to detect or investigate attacks
- In practice: missing authentication events, value error logs, no alerting on brute-force or privilege changes. logs stored where attackers can tamper with them

---

## Commands & Tools
```bash
?id=7 -> ?id=6 # attempting to change an ID in a URL to exploit IDOR

# Modified HTTP request to exploit AO3 vulnerability (fixed authentication key as data == debug in API)

POST /api/process HTTP/1.1
Host: 10.48.134.232:5003
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type:application/json
Content-Length: 22

{"data":"debug"}

```

---

## What I Learned
- Upholding IAAA is important to know who can do what, and when everything is happening; lacking in any area results in corresponding vulnerabilities (e.g. lack of accountability -> ASO9)
- OWASP Top 10 serves as great contextual understanding of web application vulnerabilities, and can be used as a framework to methodologically search for vulernabilities and enhance security
- Can recognise when ciphertext is in Base64 when alphabet matches `A-Z a-z 0-9 + / =`

---

## References (if any)
