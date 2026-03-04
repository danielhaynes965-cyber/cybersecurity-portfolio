# Wireshark: The Basic

**Path:** Cyber Security 101 > Networking  

**Date Completed:** January 4, 2026  

**Difficulty:** Easy

---

## Summary
This room introduces Wireshark as a powerful tool for deep packet inspection and network troubleshooting. It covers the essential GUI layout, navigation shortcuts, and techniques for reassembling fragmented data into human-readable conversations.

---

## Key Concepts

* The interface is divided into three primary panes: Packet List for summaries, Packet Details for layer-by-layer dissection, and Packet Bytes for hex/ASCII views.
* Capture file metadata found in Statistics provides high-level details like packet counts and hashes.
* Wireshark maps data directly to the OSI model, allowing for specific analysis from Layer 1 physical frames to Layer 5 application data.
* Logic operators such as eq, ne, and, and or enable the creation of precise display filters to isolate specific traffic.
* Following streams allows for the reassembly of fragmented packets into a coherent dialogue between a client and server.

---

## Commands & Tools
```bash
# Shortcut to jump to a specific packet number in a large capture
Ctrl + G

# Open the search menu to find strings, hex values, or display filters
Ctrl + F

# Generate an MD5 hash of exported application data for integrity verification
md5sum application_data.file

# Export specific objects like images or text files from HTTP traffic
# Path: File > Export Objects > HTTP
```

## What I Learned
- The Packet Bytes pane is essential for correlating specific protocol fields in the Details pane with their raw hex and ASCII counterparts.
- Exporting packet bytes manually is a great way to extract hidden flags or files for further analysis using hashing tools.
- Using 'Follow Stream' simplifies analysis by color-coding traffic—red for the client and blue for the server—making conversations easy to read.
- Right-clicking any detail to 'Apply as Filter' is much faster than manually typing complex filter syntax.
- Always keep an eye on the status bar to verify if your current filter is hiding too much traffic or if it has successfully isolated the target packets.

## References
- [WireShark Official User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
