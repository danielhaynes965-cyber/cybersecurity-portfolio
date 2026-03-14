# Subdomain Enumeration
**Path:** Jr Penetration Tester > Introduction to Web Hacking

**Date Completed:** Mar 14th, 2026

**Difficulty:** Easy

---

## Summary
Subdomain enumeration is the process of finding valid subdomains for a domain to expand our attack surface to try and discover more potential points of vulnerability. This room explores three different subdomain enumeration methods: Brute Force, OSINT (Open-Source Intelligence) and Virtual Host.

---

## Key Concepts
- CA (Certificate Authority) logs are publicly accessible logs of every SSL/TLS certificate created for a domain name, which can be used to discover subdomains
- Subdomains can be DNS brute
- Many important subdomains, often desireable ones from the perspective of a pentester, aren't always hosted in publically accessible DNS results
- Most modern web servers use Virtual Hosting to save resources; HOST header is used to differentiate which domain to serve
---

## Commands & Tools
```bash

site:*.tryhackme.com -site:www.tryhackme.com # google search to reveal subdomains for tryhackme.com

gobuster dns -d example.com -w /usr/share/wordlists/subdomains.txt # basic subdomain discovery automation using gobuster - will only find subdomains with public dns resolution (in the 'phonebook')

	# dns: Specifies DNS mode
	# -d: Target domain
	# -w: Path to the wordlist

./sublist3r.py -d example.com # using sublis3r to automatically enumerate subdomains

ffuf -w /path/to/wordlist -H "Host: FUZZ.domainname" -u http://[IP] # subdomain discovery via virtual host fuzzing

	# -w switch to specify the wordlist we are going to use\
	# -H switch adds/edits a header (in this instance, the Host header)
	# FUZZ keyword in the space where a subdomain would normally go; where options from the wordlist will be tried

	# can use -fs to exclude the common length 

gobuster vhost -u http://target.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt # Vhost fuzz using gobuster

	# will need to use --xl (exclude length) to remove find the needle in the haystack (same as -fs)


```

---

## What I Learned
- Dorking (Google advanced search) can be a good way to look for subdomains that are publically accessible
- DNS or direcrtory bruteforcing with a wordlist using a tool like gobuster is a good way to automatically enumerate subdomains
	- On gobuster, dir is for files/directories, dns is for subdomain discovery
	- dir uses HTTP requests, whilst dns uses DNS resolver queries
- /etc/hosts (or c:\windows\system32\drivers\etc\hosts file for Windows users) maps domain names to IP addresses
- “Security through obscurity” means trying to keep something safe mainly by keeping how it works secret.
- Virtual Host (VHost) Fuzzing works because developers often assume that if a subdomain isn't pointed to by a public DNS record, no one can find it
	- The HOST Header of an HTTP packet tells the server which website/content to give, since there are multiple websites being hosted on the same IP
		- This header is the domain (and subdomain) from the URL
	- Even if this subdomain isn't available via DNS, if it still running, then it can be disovered my manually setting it as the HOST header
	- A subdomain like this would be inaccessible from the browser (as it is DNS reliant), thus a common 'Security through Obscurity' flaw

		 

---

## References (if any)
- [Searchable database of CA logs](https://crt.sh/)
- [Automatic OSINT subdomain discovery (sublist3r)](https://www.kali.org/tools/sublist3r/)
