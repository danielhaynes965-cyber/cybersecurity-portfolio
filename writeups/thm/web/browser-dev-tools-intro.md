# Walking An Application

**Path:** Jr Penetration Tester > Introduction to Web Hacking  

**Date Completed:** Mar 10, 2026  

**Difficulty:** Easy

---

## Summary
This room teaches you how to manually inspect a web application using only your browser—no automated scanners required. It highlights how much information can be uncovered through page source, directory structure, developer tools, and network requests.

---

## Key Concepts
- Page Source can reveal hidden links, comments, frameworks, and clues.
- Browser Developer Tools (Inspector, Debugger, Network) can be used to bypass UI restrictions or reveal hidden content.    

---

## Commands & Tools
```bash
# Basic directory enumeration (optional enhancement beyond browser tools)
dirsearch -u http://TARGET-IP/             # Found /assets directory in writeups
# Viewing downloaded files
unzip tmp.zip                              # Extract framework changelog archive
cat flag.txt                                # Read the flag inside the extracted files
```

## What I Learned
- HTML comments can leak sensitive information, including paths to unfinished or hidden pages.
- Secret links embedded in source code are easy to find 
- Directory listing misconfigurations can expose internal files and flags.
- Developer Tools can reveal hidden text, bypass UI restrictions, and expose JavaScript logic
- Framework version leaks and outdated software can lead to downloadable artifacts that expose sensitive information.
