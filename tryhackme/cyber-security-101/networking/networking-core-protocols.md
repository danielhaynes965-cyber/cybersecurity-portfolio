# Networking Core Protocols

**Path:** Cyber Security 101 > Networking 

**Date Completed:** December 28, 2025  

**Difficulty:** Easy

---

## Summary
This room explores the critical Application Layer protocols that facilitate web browsing, file transfers, and email communication. It focuses on the mapping of domain names to IP addresses and the specific methods used to interact with various network services.

---

## Key Concepts
* DNS operates at Layer 7 to translate human-readable domain names into machine-readable IP addresses.

* Web traffic is handled by HTTP on port 80 in cleartext or HTTPS on port 443 with TLS encryption.
* FTP is optimized for file transfers using port 21 for command signaling and specific verbs for data movement.
* Email delivery is segmented into sending protocols like SMTP and receiving protocols like POP3 and IMAP.
* WHOIS services provide a method to query registration databases for domain ownership and IP block information.

---

## Commands & Tools
```bash
# Query DNS records to map a domain to an IP address
nslookup google.com
dig google.com

# Interact with web servers or retrieve resources via the CLI
curl [http://10.10.10.10] # curl assumes HTTP by default so can just write the IP
telnet 10.10.10.10 80 # Manually issue GET / HTTP/1.1

# Connect to an FTP server to manage files
ftp 10.10.10.10
# Common FTP verbs: USER, PASS, RETR (download), STOR (upload)

# Send a raw email using SMTP commands via telnet
telnet 10.10.10.10 25
# SMTP flow: HELO, MAIL FROM, RCPT TO, DATA

# Retrieve domain registration details
whois tryhackme.com
```

## What I Learned
- DNS records are categorized into specific types such as A for IPv4, AAAA for IPv6, and MX for mail servers.
- HTTP methods like POST and PUT allow users to submit or update data rather than just retrieving it with GET.
- SMTP handles the outgoing transfer of mail while POP3 and IMAP manage how that mail is stored and accessed by the client.
- Manual interaction with these protocols via Telnet is a powerful way to debug services or verify header responses.
- Standardized port numbers like 53 for DNS and 25 for SMTP are the default gateways for core internet functionality.
