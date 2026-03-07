# Hashing Basics

**Path:** Cyber Security 101> Cryptography  

**Date Completed:** January 9, 2026  

**Difficulty:** Easy  

---

## Summary
* This room focuses on hashing as a one-way cryptographic function used to ensure data integrity and secure password storage. It distinguishes hashing from encryption, emphasizes key mathematical properties, and provides practical experience with industry-standard cracking tools like John the Ripper and Hashcat.

---

## Key Concepts
* Hashing is designed to be mathematically impossible to reverse, unlike encryption which is two-way.
* A specific input will always produce the exact same hash output.
* A secure hash algorithm must make it extremely difficult for two different inputs to produce the same digest.

* Salting is a defense mechanism where a random string is added to a password before hashing to defeat rainbow tables

### Common Hashing Algorithms
| Algorithm | Output Length | Status | Use Case |
| :--- | :--- | :--- | :--- |
| MD5 | 128-bit | Insecure | Legacy checksums |
| SHA-1 | 160-bit | Insecure | Older digital signatures |
| SHA-256 | 256-bit | Secure | Modern certificates / Bitcoin |
| SHA-512 | 512-bit | Secure | High-security environments |
| NTLM | 128-bit | Weak | Windows password storage |

---

## Commands & Tools
```bash
# Identify the likely algorithm of a hash string
hashid -m <hash>
hash-identifier

# Crack MD5 hashes using John the Ripper and the Rockyou wordlist
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Display cracked passwords stored in the John potfile
john --show hash.txt

# Crack SHA-256 hashes using Hashcat (Mode 1400)
hashcat -m 1400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

---

## What I Learned
- Hashing is for verifying that data hasn't changed (Integrity), while encryption is for keeping data secret (Confidentiality)
- Salts do not need to be secret; they are stored in the database alongside the hash but effectively randomize the output to stop pre-computed attacks
- Algorithms like Bcrypt (identified by $2a$ or $2y$) are intentionally computationally expensive to slow down brute-force attempts
- You can often identify the hashing method by the prefix; for instance, $1$ typically indicates MD5-based Unix hashes, while $6$ indicates SHA-512.
- HMAC are "Keyed-Hash Message Authentication Codes" that provide both integrity and a way to authenticate the sender using a secret key.
