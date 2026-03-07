# CyberChef: The Basics

**Path:** Cyber Security 101 > Defensive Security Tooling  

**Date Completed:** 28/02/2026  

**Difficulty:** Easy

---

## Summary
This room introduced the tool CyberChef, a 'swiss army knife' of cyber activites. It has a plethora of useful capalities organsied in a convenient layout, many of which will be useful in future rooms and CTFs.

---

## Key Concepts
- The tool is split into four main sections: *Operations*, *Recipie*, *Input*, and *Output*
- 'Swiss Army Knife' like tool - includes a suprising amount of functionality in a tidy interface

---

## Commands & Tools
```plaintext

# Data Encoding & Decoding

To Base64          - Encodes data into Base64 format.
From Base64        - Decodes Base64 strings (essential for script analysis).
To Hex             - Converts strings/bytes to Hexadecimal.
From Hex           - Converts Hex back to raw strings.
URL Decode         - Converts %20 style characters back into plain text.
To Binary          - Converts data into 0s and 1s.

# Encryption & Hashing

MD5 / SHA-1 / SHA-256 - Generates file/string hashes for IOC (Indicator of Compromise) matching.
AES Decrypt           - Decrypts data using a provided key and IV (Initialisation Vector).
XOR                   - A common, simple obfuscation method used by malware.
ROT13                 - Simple letter substitution cipher.

# Data Extraction (The "Magic" Tools)

Extract IP addresses  - Pulls all IPv4 and IPv6 addresses from a block of text.
Extract URLs          - Finds all web links within the input.
Extract Email         - Pulls email addresses from data.
Strings               - Extracts printable strings from binary data (similar to the Linux 'strings' command).
Regular Expression    - Allows you to define your own search patterns using Regex.

# Formatting & Logic

To Hexdump            - Formats data into a classic hex/ASCII side-by-side view.
From Hexdump          - Reverses a hexdump back into raw data.
JSON Beautify         - Takes minified/messy JSON and adds indentation/newlines.
Strip HTML tags       - Removes all HTML code, leaving only the text content.
Find / Replace        - Standard text manipulation.

# Useful Operation

Magic                 - Automatically detects encoding/encryption and suggests the correct recipe.

```

---

## What I Learned
- Search is useful to find operations
- The power of CyberChef isn't just the tools, it's the ability to stack them in the *Recipie* section
- Can import input and export output
- Recipies can be saved
- Multiple input tabs can be used
- 'Auto-bake' saves you having to press 'Bake' every time

---

## References
- (https://gchq.github.io/CyberChef/)
