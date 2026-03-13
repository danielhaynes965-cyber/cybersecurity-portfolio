# Content Discovery

**Path:** Jr Penetration Tester > Introduction to Web Hacking

**Date Completed:** Mar 13th, 2026  

**Difficulty:** Easy

---

## Summary
This room teaches the various ways of discovering hidden or private content on a webserver that could lead to new vulnerabilities. There are three main ways of discovering content on a website which are covered: Manually, Automated and OSINT (Open-Source Intelligence).

---

## Key Concepts
- Content Discovery is the unvovering of 'content' (files, videos, pictures, backups, a website features, etc...) that aren't immediately presented to us and that weren't always intended for public access.
- The discover of some content often leads to more subsequent discovery as a result
- OSINT is a term to describe external resources available that can help in discovering information about your target website
- Google Hacking/Dorking is using Google's advanced search features to uncover information on the internet
- Git is a version control system that tracks changes to files in a project (useful for teamwork on software developement projects)
- S3 Buckets are a storage service provided by Amazon AWS, allowing people to save files and even static website content in the cloud accessible over HTTP and HTTPS
- Automated discovery is the process of using tools to discover content rather than doing it manually
---

## Commands & Tools
```bash

curl https://domain/path/to/favicon | md5sum # get md5 hash of favicon to compare to OWASP list

curl http://[IP] -v # verbose curl to get HTTP headers
```

### Google Hacking AKA Dorking

| **Filter** | **Example** | **Description** |
|---|---|---|
| site | site:tryhackme.com | returns results only from the specified website address |
| inurl | inurl:admin | returns results that have the specified word in the URL |
| filetype | filetype:pdf | returns results which are a particular file extension |
| intitle | intitle:admin | returns results that contain the specified word in the title |

---

## What I Learned

- Append `/robots.txt` to the end of a domain to see a great list of locations on the website that owners don't want people to access
- Can do the same with `/sitemap.xml`. This gives a list of every file the website owner wishes to be listed on a search engine (can potentially be some 'content' discover)
- The 'favicon' is a small icon displayed in the browser's address bar or tab used for branding a website. Default favicons can indicate which framework is being to used to build the website
- HTTP headers sometimes contain useful information such as the webserver software and possibly the programming/scripting language in use
- Wappalyzer is a browser extension that helps identify what technologies a website uses (e.g. frameworks, Content Management Systems (CMS), payment processors, version numbers etc...) 
- GitHub's search feature can be used to look for company names or website names to try and locate repositories belonging to your target.
- The format of the S3 buckets is http(s)://{name}.s3.amazonaws.com where {name} is decided by the owner (access permissions can be incorrectly set)
- The Wayback Machine is an archive of website that date back to the late 90s; can help uncover old pages that may still be active on the current website
---

## References
- [OWASP's list of common framework favicons (md5sum)](https://wiki.owasp.org/index.php/OWASP_favicon_database)
- [Wappalyzer](https://www.wappalyzer.com/)
- [The Wayback Machine]	(https://archive.org/web/)
