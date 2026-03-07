# Public Key Encryption Basics

**Path:** Cyber Security 101 > Cryptography  

**Date Completed:** January 8, 2026  

**Difficulty:** Easy  

---

## Summary
This room explores the foundational mechanics of asymmetric and symmetric encryption. It breaks down the mathematical logic behind RSA and the Diffie-Hellman key exchange while providing practical tools for managing keys and certificates.

---

## Key Concepts

#### Symmetric Encryption (Private Key)
- Pros: Fast, efficient for large amounts of data.
- Cons: Key distribution is difficult (how do you share the key securely?).
- Examples:
  - DES: Old standard (1977), 56-bit key. Now insecure (broken in < 24 hours).
  - 3DES: Applies DES three times. Deprecated in 2019.
  - AES: The current gold standard (2001). Supports key sizes of 128, 192, or 256 bits.

#### Asymmetric Encryption (Public Key)
- Logic: Data encrypted with the Public Key can only be decrypted by the corresponding Private Key.
- Pros: Solves the key distribution problem.
- Cons: Much slower than symmetric encryption; uses much larger keys (2048–4096 bits).
- Examples: RSA, ECC (Elliptic Curve Cryptography), Diffie-Hellman.

#### RSA Variables & Operations
```
RSA security relies on the mathematical difficulty of factoring large prime numbers p and q.
The modulus n is calculated by multiplying p and q (n = p * q).
Euler's Totient phi(n) is calculated as (p-1) * (q-1).
The public exponent e is typically set to 65537.
The private exponent d is the modular inverse of e mod phi(n).
Encryption is performed using the formula: c = m^e mod n.
Decryption is performed using the formula: m = c^d mod n.
```
#### Diffie-Hellman Key Exchange
```
Parties establish a shared secret over insecure channels using a public base g and prime p.
Alice chooses a private key a and Bob chooses a private key b.
Alice generates a public key A = g^a mod p.
Bob generates a public key B = g^b mod p.
The shared secret S is calculated as S = B^a mod p by Alice and S = A^b mod p by Bob.
```

---

## Commands & Tools
```bash
# Generate a new key pair using RSA or ED25519 algorithms
ssh-keygen -t [algorithm]

# Log in to a remote host using a specific private key file
ssh -i [private_key] user@host

# Import a public or backup key into the GPG keyring
gpg --import [keyfile]

# Decrypt a GPG-encrypted file
gpg --decrypt [file].gpg

# Automate attacks on weak RSA keys in CTF environments
RsaCtfTool
```

---

## What I Learned
* Digital signatures involve encrypting a hash with a private key to prove authenticity and non-repudiation.
* Certificates are used by servers to prove identity and are verified by a trusted Certificate Authority (CA).
* Let's Encrypt is a standard resource for obtaining free TLS certificates to secure web traffic.
* In RSA, m represents the plaintext message while c represents the resulting ciphertext.
* Modulo (MOD) and Exclusive Or (XOR) are common opperators used in symmetric encryption
