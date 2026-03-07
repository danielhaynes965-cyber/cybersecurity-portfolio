# Gobuster: The Basics

**Path:** Cyber Security 101 > Offensive Security Tooling

**Date Completed:** Jan 25, 2026  

**Difficulty:** Easy

---

## Summary
Gobuster is a high-performance tool used to discover "hidden" attack surfaces by brute-forcing URIs, DNS subdomains, and Virtual Hosts. It relies on wordlists to systematically guess valid resources that are not explicitly linked on a website.

---

## Key Concepts
* **Operating Modes:**
    * `dir`: Enumerates directories and files on a web server.
    * `dns`: Brute-forces subdomains for a specific domain.
    * `vhost`: Brute-forces Virtual Hosts (Host headers) against an IP or domain.
* CTFs often require manual DNS resolution. If a hostname like `offensivetools.thm` doesn't resolve, it must be added to `/etc/hosts` with the target IP.
* **Status Codes as Signal:**
    * **200 (OK):** Direct hit; content exists.
    * **301/302 (Redirect):** Indicates a folder or moved resource; worth following.
    * **401/403 (Unauthorized/Forbidden):** Often "gold"—indicates a restricted area like an admin panel.

---

## Commands & Tools

### Directory & File Enumeration (`dir`)
```bash
# Standard directory scan
gobuster dir -u [http://target.thm/](http://target.thm/) -w /usr/share/wordlists/dirb/common.txt

# Scan for specific file extensions
gobuster dir -u [http://target.thm/](http://target.thm/) -w common.txt -x php,txt,js,bak

# Common Flags
-u  # Target URL
-w  # Path to wordlist
-x  # File extensions (comma-separated)
-t  # Threads (Default 10; increase for speed)
-o  # Output results to a file
```
### DNS & VHost Enumeration
```bash
# Subdomain Discovery (DNS mode)
gobuster dns -d target.thm -w subdomains.txt

# Virtual Host Discovery (vhost mode)
# Used when multiple sites share one IP via different Host headers
gobuster vhost -u [http://target.thm](http://target.thm) -w subdomains.txt
```
### Recommended Wordlists (Kali/SecLists)
- Web Content (Fast): /usr/share/wordlists/dirb/common.txt
- Web Content (Medium): /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
- DNS/Subdomains: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

---
## References
- [Gobuster GitHub Repository](https://github.com/OJ/gobuster)
- [SecLists - The Ultimate Wordlist Collection](https://github.com/danielmiessler/SecLists)
