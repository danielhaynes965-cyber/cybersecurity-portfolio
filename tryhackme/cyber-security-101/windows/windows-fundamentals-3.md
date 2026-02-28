# Windows Fundamentals 3

**Path:** Cyber Security 101 > Windows Fundamentals

**Date Completed:** 15 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room focuses on Windows security features, including updates, antivirus, firewall profiles, SmartScreen, TPM, BitLocker, and VSS. These components form the defensive layers that protect Windows systems from malware, exploitation, and data loss.

--- 

## Key Concepts 
- Windows Updates: Patch Tuesday, forced updates, and security patches.
- Windows Security dashboard and its status indicators.
- Defender Antivirus: real-time protection, scan types, and exclusions.
- Firewall profiles: Domain, Private, Public.
- SmartScreen and exploit protection.
- Device Security: Core Isolation, Memory Integrity, TPM.
- BitLocker encryption and TPM requirements.
- VSS for backups and system restore.

--- 

## Commands & Tools 
```bash
# Windows Firewall Advanced Settings
wf.msc

# Open Windows Security
windowsdefender://

# Manage BitLocker
control.exe /name Microsoft.BitLockerDriveEncryption

```

---

## What I Learned
- Windows updates are unavoidable and essential for security.
- Defender’s real-time protection and scan options are more capable than many assume.
- Firewall profiles change depending on network trust level.
- TPM enables secure key storage and is required for BitLocker by default.
- VSS underpins restore points and backup snapshots. 
