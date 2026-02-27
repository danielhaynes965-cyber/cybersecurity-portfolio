# Windows Command Line

**Path:** Cyber Security 101 > Command Line

**Date Completed:** 20 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room introduces essential Windows command‑line utilities for system enumeration, network diagnostics, file management, and process control. These commands form the baseline toolkit for troubleshooting, system administration, and early‑stage incident response.

--- 

## Key Concepts 
- System information gathering using `ver`, `systeminfo`, `driverquery`, and built‑in help.
- Network diagnostics with ipconfig, `ping`, `tracert`, `nslookup`, and `netstat`.
- File system navigation and manipulation using `dir`, `cd`, `md`, `rd`, `copy`, `del`, and `ren`.
- Process and task management with `tasklist` and `taskkill`.
 
--- 

## Commands & Tools 
```cmd
# System info
ver
systeminfo | more
driverquery | more
help ipconfig
cls

# Network troubleshooting
ipconfig /all
ping google.com
tracert google.com
nslookup tryhackme.com
netstat -ano

# File & disk management
dir
cd C:\Windows
mkdir testfolder
rmdir testfolder
copy file.txt C:\temp
del file.txt
ren old.txt new.txt
chkdsk C:

# Process management
tasklist
taskkill /IM notepad.exe
taskkill /PID 1234

```

---

## What I Learned
- `systeminfo` and `driverquery` are powerful for quick host profiling during investigations.
- `ipconfig /all` reveals critical details like MAC addresses, DHCP status, and DNS servers.
- `netstat -ano` is essential for identifying suspicious listening ports and mapping them to PIDs.
- Basic file commands (`copy`, `del`, `ren`) are still the fastest way to manipulate files during troubleshooting.
- `tasklist` and `taskkill` provide lightweight process control without needing Task Manager.
