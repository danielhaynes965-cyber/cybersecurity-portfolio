# tcpdump: The Basics

**Path:** Cyber Security 101 > Networking 

**Date Completed:** January 5, 2026  

**Difficulty:** Easy

---

## Summary
This room introduces `tcpdump` as the industry-standard command-line tool for capturing and analyzing network traffic. It focuses on mastering fundamental syntax, output formatting, and the application of complex filters to isolate specific packets in a live environment.

---

## Key Concepts
* Data acquisition relies on selecting the correct interface and defining capture limits to prevent system resource exhaustion.
* Formatting flags allow an analyst to balance the speed of raw data with the readability of Hex and ASCII translations.
* Filter expressions utilize boolean logic to pinpoint traffic by host, port, or subnet, effectively removing "noise" from the analysis.
* The utility functions as both a real-time monitor and a recorder, allowing raw packets to be saved and reviewed later in tools like Wireshark.


---

## Commands & Tools
```bash
# Basic Structure
tcpdump [options] [filter-expression]

# Data Acquisition & Output
-i [interface] # Listens on a specific interface (e.g., eth0). Use any for all interfaces.
-D # Lists all available interfaces.
-c [number] # Captures a specific number of packets and then stops.
-w [file.pcap] # Writes the captured raw packets to a file.
-r [file.pcap] # Reads and processes packets from a saved file.

# Formatting & Verbosity
-n # Disables name resolution (displays IP addresses instead of hostnames). Highly recommended for speed.
-nn # Disables both name and port resolution (displays port numbers instead of service names).
-v, -vv, -vvv # Increases the level of detail/verbosity in the output.
-X # Displays packet content in both Hex and ASCII.
-A # Displays packet content in ASCII only (useful for reading web traffic or cleartext credentials).
-q # "Quiet" mode; shows less protocol information.
-e # Includes Ethernet header information (MAC addresses).

# Filter Expressions; can be combined using logic: and (&&), or (||), and not (!).
host [IP] # Filters traffic to or from a specific IP.
src [IP] / dst [IP] # Filters by source or destination address.
port [number] # Filters traffic on a specific port (e.g., port 80).
net [network/CIDR] # Filters traffic from a specific subnet (e.g., net 192.168.1.0/24).
icmp # Captures only ICMP (ping) traffic.
tcp # Captures only TCP traffic.
udp # Captures only UDP traffic.
arp # Captures Address Resolution Protocol traffic.

```

---

## What I Learned
* Disabling name resolution with `-n` or `-nn` is a critical "gotcha" to remember because it prevents the tool from hanging during heavy traffic.
* The `-A` flag is a powerful shortcut for identifying cleartext credentials or reading web traffic without needing a full protocol dissector.
* Using `-e` provides the Layer 2 perspective by including MAC addresses, which is essential for troubleshooting local link issues or ARP spoofing.
* Combining filters with `and`, `or`, and `not` allows for surgical precision, such as excluding your own management IP to see only target traffic.
* Capturing a specific number of packets with `-c` is a safe practice to ensure you don't fill up disk space during long-term monitoring sessions.

---

## References (if any)
- [tcpdump Manual Page](https://www.tcpdump.org/manpages/tcpdump.1.html)
