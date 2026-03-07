# Active Directory Basics

**Path:** Cyber Security 101 > Windows Fundamentals

**Date Completed:** 17 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room introduces the foundational components of Active Directory, including domains, objects, authentication, and administrative structures. It matters because AD is the backbone of enterprise Windows environments, and understanding it is essential for system administration, security, and penetration testing.

--- 

## Key Concepts
- AD centralizes management of users, computers, and resources through a Domain Controller.  
- Objects include users, machines, groups, and OUs, each serving a specific organizational purpose.  
- Delegation allows limited administrative rights without granting full domain admin privileges.  
- GPOs enforce configuration and security policies across the domain.  
- Kerberos is the primary authentication protocol, with NTLM retained for legacy support.  
- Forests, trees, and trusts define how multiple domains interconnect and share resources.

--- 

## Commands & Tools 
```powershell
# Reset a user's password (PowerShell)
Set-ADAccountPassword -Identity username

# Unlock a user account (PowerShell)
Unlock-ADAccount -Identity username

# Group Policy Management Console
gpmc.msc

# Local Group Policy Editor
gpedit.msc

# Domain and Trusts Management
domain.msc

```

---

## What I Learned
- AD objects follow a strict hierarchy, and OUs are essential for applying GPOs and delegating control.
- Delegation is powerful: you can give helpdesk staff limited rights without exposing the domain.
- Kerberos uses ticketing, making it more secure and efficient than NTLM.
- SYSVOL replication ensures GPOs are consistent across domain controllers.
- Trust relationships define how domains interact and share authentication.
