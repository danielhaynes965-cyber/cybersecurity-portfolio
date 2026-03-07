# Networking Essentials

**Path:** Cyber Security 101 > Networking

**Date Completed:** December 28, 2025  

**Difficulty:** Easy  

---

## Summary
This room covers the essential protocols that manage device identity and traffic flow within a network. It provides a deep dive into how devices obtain IP addresses, map hardware addresses, and communicate across different network boundaries.


---

## Key Concepts
* DHCP automates the configuration of IP addresses, subnet masks, gateways, and DNS settings to prevent manual addressing errors.
* The DORA process (Discover, Offer, Request, Acknowledge) defines the specific handshake between a client and a DHCP server.
* ARP bridges the gap between logical Layer 3 IP addresses and physical Layer 2 MAC addresses so data reaches the correct hardware on a local link.
* ICMP acts as a diagnostic layer for troubleshooting connectivity through echo requests and path tracing.
* NAT allows an entire private network to share a single public IP address by modifying packet headers as they exit the local gateway.

---

## Commands & Tools
```bash
# Test connectivity by sending 4 ICMP Echo Request packets
ping -c 4 [target_ip]

# Map the path to a destination by incrementing the TTL of packets
traceroute [target_ip]

# Display the local ARP table to see IP-to-MAC address mappings
arp -a
```

---

## What I Learned
- The DORA sequence is the standard lifecycle for a device joining a network and receiving its identity.
- ARP requests are sent as a broadcast to all devices on the segment, but the reply is a direct unicast message from the owner of the IP.
- Traceroute identifies the specific routers in a path by intentionally timing out packets using TTL increments.
- Ping relies on specific ICMP types, specifically Type 8 for requests and Type 0 for replies.
- NAT is the critical technology that enables private home networks to function using the limited pool of public IPv4 addresses.

## References
- IETF RFC 2131: https://datatracker.ietf.org/doc/html/rfc2131
- How NAT Works (Cisco Documentation): https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html
