# REMnux: Getting Started

**Path:** Cyber Security 101 > Defnsive Security Tooling

**Date Completed:** Mar 8, 2026

**Difficulty:** Easy

---

## Summary
This room introduces REMnux, a linux distribution focused on malware analysis. The room goes over the primary tools included in the distro, covering dynamic and static analysis.
 
---

## Key Concepts
- REMnux is a linux distribution designed for malware analysis, containing tools scuh as Volatility, YARA, Wireshark, oledump, and INetSim
- Static analysis is a technique that involves an algebraic examination of source code without executing it
- Dynamic analysis is the process of analyzing malware by running it in a controlled environment like a sandbox
- JavaScript Object Notation (JSON) is an open standard file and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays
### OLE
- OLE stands for Object Linking and Embedding, a proprietary technology developed by Microsoft
- OLE2 files are typically used to store multiple data types, such as documents, spreadsheets, and presentations, within a single file
- `oledump.py` is handy for extracting and examining the contents of OLE2 files, making it a valuable resource for forensic analysis and malware detection
### INETSim: Internet Services Simulation Suite
- Facilitates dynamic analysis
- Must configure the tool INetSim inside REMnux before use (see below)
- Can be combined with tools like Burp Suite for SSL interception, as INetSim's native SSL support is limited
### Volatility & Strings
- Used when dealing with memory images as evidence
- Volatility commands are executed to identify and extract specific artefacts from memory images, and the resulting output can be saved to text files for further examination
- strings is a command-line tool that searches for printable strings in binary files, including executables and memory images
- Little endian is a byte order where the least significant byte is stored at the lowest memory address
- Big endian is a byte order where the most significant byte is stored at the lowest memory address
---

## Commands & Tools
```bash
# oledump

oledump.py <file> # Conduct static analysis on potentially malicious documents

oledump.py <file> -s 4 # Run the oledump and look into the actual data stream of interest (-s short for -select, then an integer)

oledump.py <file> -s 4 --vbadecompress # Automatically decompress any compressed VBA macros it finds into a more readable format

# INETSim

	# configuration process

	sudo nano /etc/inetsim/inetsim.conf # remove the comment from #dns_default_ip 0.0.0.0 (line 207) and then change 0.0.0.0 to machine IP

	cat /etc/inetsim/inetsim.conf | grep dns_default_ip # confirm changes have saved

sudo inetsim # run the tool - if 'simulation running' message, then fake network is running

xdg-open https://[IP] # run in terminal to access INETSim homepage

sudo cat /var/log/inetsim/report/report.<num>.txt # read the report - location and name will vary

# Volatility 3

sudo vol3 -f <file> [plugin] # perform specific analysis on a memory image file

# Strimgs

strings <memory image file> > <output file> # extracts printable ASCII text

strings <memory image file> -e l

```

---

## What I Learned
- A memory image is a snapshot of a computer's memory at a specific point in time, often captured for forensic analysis
- REMnux distro is for the forensic analysis of potential malware 
- Is designed for defensive purposes but can still be useful in offensive contexts to identify weakpoints

---

## References (if any)
- [Volatility 3 Plugins](https://volatility3.readthedocs.io/en/stable/volatility3.plugins.html)
