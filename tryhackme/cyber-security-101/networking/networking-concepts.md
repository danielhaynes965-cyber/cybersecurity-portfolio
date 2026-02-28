# Networking Fundamentals

**Path:** Cyber Security 101 > Network

**Date Completed:** December 26, 2025  

**Difficulty:** Easy  

---

## Summary
This room provides a foundational understanding of how data travels across a network using the OSI and TCP/IP models. It explains the mechanics of encapsulation, the differences between connection-oriented and connectionless protocols, and basic network troubleshooting tools.



---

## Key Concepts
* Networking is structured in layers to standardize communication between diverse hardware and software.
* The OSI model serves as the theoretical framework, whereas the TCP/IP model is the practical implementation used in modern networking.
* Encapsulation wraps data in specific headers at each layer to ensure accurate delivery and routing.
* TCP provides reliable, connection-oriented communication, while UDP prioritizes speed through a connectionless approach.

---

## Commands & Tools
```bash

# Connect to a remote service via Telnet to test connectivity/ports
telnet [IP_ADDRESS] [PORT]

# Example: Testing an HTTP server manually
telnet 10.10.x.x 80
GET / HTTP/1.1
Host: telnet.thm
# (Note: Press Enter twice after the Host header to send the request)

# Example: Checking an Echo server (Port 7)
telnet 10.10.x.x 7

# Example: Checking a Daytime server (Port 13)
telnet 10.10.x.x 13

```

---

## What I Learned

* Manual HTTP requests via Telnet require two consecutive Enter key presses to signal the end of the header block.
* The TCP three-way handshake (SYN, SYN/ACK, ACK) is essential for establishing a synchronized connection before data transfer.
* Routers primarily operate at the Network Layer (IP) and swap Link Layer (MAC) headers at each hop.
* UDP is the preferred protocol for services like DNS and streaming where minor data loss is preferable to transmission delays.
