# Windows Fundamentals 1 

**Path:** Cyber Security 101 > Windows Fundamentals

**Date Completed:** 3 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room introduces the core structure of the Windows operating system, including editions, the GUI, NTFS, permissions, and essential system utilities. It matters because these fundamentals underpin everything from system administration to security hardening and troubleshooting.

--- 

## Key Concepts 
- Differences between Windows Home vs Pro and the evolution of Windows versions.
- GUI components: Start Menu, Taskbar, notifications, and where system settings live.
- NTFS features: ACLs, permissions, and Alternative Data Streams as a security concern.
- Importance of the System32 directory for OS stability.
- User account types and how UAC enforces least privilege.
- Task Manager as a core diagnostic and monitoring tool.

--- 

## Commands & Tools 
```bash
# View local users and groups
lusrmgr.msc

# Open Task Manager
Ctrl + Shift + Esc

# Access Control Panel (legacy settings)
control.exe

```

---

## What I Learned
- NTFS permissions are granular and essential for securing files and folders.
- ADS can hide malicious content, making it a common red-team technique.
- UAC ensures even admins don’t run with full privileges by default.
- System32 is critical; deleting or modifying files here can break the OS.
- Task Manager is more than a process killer; it’s a performance and resource monitor.
