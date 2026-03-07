# John The Ripper Basics

**Path:** Cyber Security 101 > Cryptography  

**Date Completed:** January 10, 2026  

**Difficulty:** Easy 

---

## Summary
* This room covers the fundamental operations of John the Ripper (JTR), a versatile multi-platform password cracking tool. 

---

## Key Concepts
* 'Single Crack Mode' is a high-speed mode that uses "word mangling" based on account usernames to find common variations.
* 'Wordlist Mode' is the standard cracking method that compares hashes against massive lists of known passwords like rockyou.txt.
* 'Incremental Mode' is brute-force approach that attempts every possible character combination; powerful but extremely time-consuming.

* Linux security architecture separates user metadata (/etc/passwd) from actual hashes (/etc/shadow), requiring a merge before cracking.
* Specialized scripts allow JTR to target local files (ZIP, PDF, SSH keys) by isolating their cryptographic components.

---

## Commands & Tools

```bash
# Execute Single Crack mode for fast, name-based mangling
john --single <hash_file>

# Run a wordlist-based attack
john --wordlist=/usr/share/wordlists/rockyou.txt <hash_file>

# Restore a previously interrupted cracking session
john --restore

# Linux: Merge passwd and shadow files into a crackable format
unshadow /etc/passwd /etc/shadow > combined.txt

# Windows: Force NTLM format for Windows hash files
john --format=NT --wordlist=rockyou.txt <hash_file>

# Extract hash from a ZIP archive
zip2john file.zip > hash.txt

# Extract hash from an SSH private key
ssh2john id_rsa > hash.txt
```

---

## What I Learned
* JTR requires the context of /etc/passwd to correctly associate hashes from /etc/shadow with their respective usernames.
* Pressing the spacebar during a live session provides a real-time status update without interrupting the cracking process.
* Cracked passwords are saved in john.pot; always use the --show flag rather than reading the potfile directly to ensure correct formatting.
* Applying --rules to a wordlist allows JTR to automatically try permutations like substituting characters (e.g., 's' to '$') or appending years.
* While JTR is excellent at auto-detecting hash types, using --list=formats is a good troubleshooting step if the tool fails to recognize a specific input.

---

## References
- [John the Ripper Official Documentation](https://www.openwall.com/john/doc/)
