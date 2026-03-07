# Firewall Fundamentals

**Path:** Cyber Security 101 > Secrutiy Solutions  

**Date Completed:** Feb 27, 2026  

**Difficulty:** Easy

---

## Summary
This room introduces the different layers of network defense, from basic packet filtering to advanced Application-Layer inspection. Understanding these technologies is vital for both hardening a system and identifying bypass techniques like ACK spoofing or WAF evasion.

---

## Key Concepts
* Stateless firewalls treat packets in isolation, while Stateful firewalls maintain a "state table" to track active sessions.
* Proxy firewalls act as intermediaries (terminating connections), while Next-Generation Firewalls (NGFW) perform Deep Packet Inspection (DPI) across multiple OSI layers.
* Rules are defined by a 5-tuple: Source IP, Destination IP, Source Port, Destination Port, and Protocol (TCP/UDP/ICMP).
* A WAF (Web Application Firewall) is a specialized Layer 7 defense focused on neutralizing web-specific attacks like SQLi and XSS.

---

## Commands & Tools
```bash
# --- Linux UFW (Uncomplicated Firewall) ---
# Check status with numbered rules for easy management
sudo ufw status numbered

# Allow specific service (SSH) on TCP
sudo ufw allow 22/tcp

# Deny all outgoing traffic (Hardening)
sudo ufw default deny outgoing

# Delete a specific rule by its number
sudo ufw delete 2

# --- WAF Fingerprinting ---
# Identify if a web target is behind a WAF
wafw00f [http://target.com](http://target.com)

# Nmap script to detect WAF presence
nmap -p80 --script http-waf-fingerprint target.com
```

## What I Learned 
- In a CTF, if a firewall is stateless, sending packets with the ACK flag set can sometimes trick the device into thinking the packet is part of an established stream, allowing it to pass.
- The most secure posture is to deny all traffic by default and only explicitly allow what is necessary (Least Privilege).
- Windows Defender uses different rule sets for "Public" vs "Private" networks; an attacker on a local network might have more success if the target thinks it is on a "Private" home network.
- A Proxy firewall actually breaks the connection between the client and server, acting as a middleman, which provides the highest level of inspection but adds latency.
