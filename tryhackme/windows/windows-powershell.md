# Windows PowerShell

**Path:** Cyber Security 101 > Command Line

**Date Completed:** 20 Dec, 2025

**Difficulty:** Easy

--- 

## Summary 
This room introduces PowerShell as a modern, object‑oriented automation and administration shell built on .NET. It focuses on discovery cmdlets, file and system interaction, data manipulation through pipelines, and the foundations of remote execution and scripting.

--- 

## Key Concepts 
- PowerShell treats output as objects, not text, enabling richer filtering, sorting, and selection.
- Cmdlets follow a consistent Verb‑Noun naming pattern.
- Discovery tools (Get-Help, Get-Command, Get-Alias) form the backbone of learning PowerShell.
- Pipelines pass objects between cmdlets, enabling powerful one‑liners.
- Remote execution and scripting (.ps1 files) extend PowerShell beyond local administration.

--- 

## Commands & Tools 
```powershell

# Discovery
Get-Help
Get-Process
Get-Command
Get-Alias

# File system & content
Get-ChildItem
Set-Location C:\Windows
Get-Content .\notes.txt

# Networking & processes
Get-NetTCPConnection
Get-Process
Stop-Process -Id 1234

# Data manipulation
Get-Process | Where-Object {$_.CPU -gt 50}
Get-Service | Sort-Object Status
Get-ChildItem | Select-Object Name, Length

# Remote execution & scripting
Invoke-Command -ComputerName SERVER01 -ScriptBlock { Get-Service }
# Comments
# Single-line comment
<# Multi-line
   comment #>

# Common Aliases
ls → Get-ChildItem
dir → Get-ChildItem
cd → Set-Location
pwd → Get-Location
cat → Get-Content

```

---

## What I Learned
- PowerShell’s object-based pipeline is far more powerful than CMD’s text-based output.
- `Get-Help` and `Get-Command` make PowerShell self‑documenting and easy to explore.
- Filtering with `Where-Object` and selecting properties with `Select-Object` unlock efficient data analysis.
- Remote execution via `Invoke-Command` is a core capability for enterprise administration.
- Understanding aliases helps bridge the gap between Linux‑style commands and PowerShell cmdlets. 
