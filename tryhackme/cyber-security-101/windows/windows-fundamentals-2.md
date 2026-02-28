# Windows Fundamentals 2

**Path:** Cyber Security 101 > Windows Fundamentals

**Date Completed:** 4 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room covers essential Windows administrative tools, how to access them, and what they reveal about system behavior. Understanding these tools is crucial for diagnosing issues, managing services, and inspecting system configuration.

--- 

## Key Concepts 
- MSConfig tabs: General, Boot, Services, Startup, Tools.
- Core utilities like Computer Management, Resource Monitor, and System Information.
- Registry Editor as a powerful but dangerous configuration database.
- Command Prompt as a text-based interface for system interaction.

--- 

## Commands & Tools 
```bash
# Change UAC settings
UserAccountControlSettings.exe

# Computer Management console
compmgmt.msc

# System Information
msinfo32.exe

# Resource Monitor
resmon.exe

# Registry Editor
regedit.exe

# Command Prompt
cmd.exe

```

---

## What I Learned
- MSConfig is a central place to control startup behavior and troubleshoot boot issues.
- Resource Monitor gives deeper insight than Task Manager for CPU, RAM, Disk, and Network.
- The registry is extremely powerful—changes should be deliberate and cautious.
- Computer Management consolidates many admin tools into one interface.
- Many Windows tools are accessible via .msc or .exe commands.
