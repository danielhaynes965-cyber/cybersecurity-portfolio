# Networking Secure Protocols

**Path:** Cyber Security 101 > Networking

**Date Completed:** December 28, 2025  

**Difficulty:** Easy

---

## Summary
This room explores the transition from vulnerable plaintext protocols to their encrypted counterparts using TLS and SSH. It defines the core principles of confidentiality, integrity, and authenticity while providing hands-on methods for testing secure connections.

---

## Key Concepts
* Confidentiality ensures that data remains unreadable to unauthorized parties, while integrity confirms that the data has not been modified during transit.
* Authenticity provides a mechanism to verify the identity of the server or client involved in the communication.
* TLS (Transport Layer Security) serves as the modern successor to SSL, adding a robust security layer to standard Layer 4 protocols.

* Secure protocols like HTTPS, SSH, and SFTP replace legacy services like HTTP, Telnet, and FTP to prevent data interception.
* VPNs establish an encrypted tunnel for all network traffic, ensuring both data security and anonymity by masking the user's original IP address.

---

## Commands & Tools
```bash
# Manually interact with an HTTPS service to test the secure connection
openssl s_client -connect [IP]:443

# Connect to a secure POP3S mail server using specific flags for cleaner output
openssl s_client -connect [IP]:995 -crlf -quiet

# Use Ncat to automatically manage the TLS handshake for a secure port
ncat --ssl [IP] [PORT]

# Access a remote system securely using SSH
ssh username@[IP]
```

---

## What I Learned
* Replacing Telnet (Port 23) with SSH (Port 22) is essential for preventing credentials from being captured in cleartext.
* OpenSSL's `s_client` is a vital tool for manually verifying that a secure service is configured correctly.
* SSH's ability to notify the user if a server's fingerprint changes provides a critical defense against Man-in-the-Middle (MITM) attacks.
* Key-based authentication offers a superior security posture compared to standard passwords by using cryptographic public/private key pairs.
* Moving from port 25 (SMTP) to port 465 (SMTPS) ensures that email transmissions are protected by TLS from start to finish.

---

## References
- [OpenSSL s_client Documentation](https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html)
