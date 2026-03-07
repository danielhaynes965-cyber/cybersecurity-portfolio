# Web Application Basics

**Path:** Cyber Security 101 > Web Hacking  

**Date Completed:** Jan 21, 2026  

**Difficulty:** Easy

---

## Summary
This room covers the fundamental architecture of the web, focusing on the relationship between clients, servers, and the HTTP protocol. Understanding the anatomy of URLs and the structure of HTTP messages is critical for identifying common attack vectors like injection and directory traversal.

---

## Key Concepts
* **Infrastructure:** Web Servers deliver content, Browsers interact with it, and WAFs filter malicious traffic like SQLi or XSS.
* **URL Anatomy:** Consists of the Scheme (protocol), Host (domain), Port (service), Path (resource), Query String (data pairs), and Fragment (page section).
* **Message Structure:** Both requests and responses utilize a Start Line, Headers (metadata), an Empty Line (divider), and an optional Body.
* **Statelessness & Sessions:** Servers use headers like `Set-Cookie` for session management, while security flags like `HttpOnly` and `Secure` protect these sessions from theft.

---

## Commands & Tools
### Anatomy of a Request URL

```text
[https://tryhackme.com:443/profile?id=123#settings](https://tryhackme.com:443/profile?id=123#settings)
|___|   |__________| |__| |______| |____| |______|
Scheme      Host     Port   Path    Query  Fragment
```

### HTTP Methods & Status Codes
```bash
# Common HTTP Methods used in requests
GET     # Request data from a resource
POST    # Submit data to be processed (logins/forms)
PUT     # Create or replace a resource
DELETE  # Remove a resource
OPTIONS # Check supported methods for a URL

# Common Status Code Ranges
2xx     # Success (e.g., 200 OK)
3xx     # Redirection (e.g., 301 Moved Permanently)
4xx     # Client Error (e.g., 403 Forbidden, 404 Not Found)
5xx     # Server Error (e.g., 500 Internal Server Error)
```

---

## What I Learned
- Attackers often target the Path for directory traversal and the Query String for various injection attacks.
- The Empty Line is Essential: In the HTTP message structure, the empty line serves as a mandatory divider; without it, the server cannot distinguish where headers end and the body begins.
- Response headers like Server can disclose software versions (e.g., Apache/2.4.41), helping to find specific exploits.
- Be wary of subtly misspelled domains used to trick users into visiting malicious clones.

