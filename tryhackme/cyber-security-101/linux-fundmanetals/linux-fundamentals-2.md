# Linux Fundamentals 2
**Path:** Cyber Security 101 > Linux Fundamentals
**Date Completed:** Nov 30, 2025
**Difficulty:** Easy

---

# Summary
This room expands on command usage, introduces SSH for remote access, and covers file creation, deletion, movement, and permissions. It also explains how Linux represents users, groups, and file types. These concepts matter because remote access and permission management are foundational for system administration and security.

---

# Key Concepts
- SSH provides encrypted remote access
- Flags modify command behaviour
- Linux files generally don’t rely on extensions—file type is determined by content
- Permissions define what users, groups, and others can do with a file

---

# Commands & Tools
```bash
# Remote access
ssh user@IP                 # connect to remote machine

# Flags & documentation
ls -a                       # show hidden files
command --help              # quick help
man command                 # full manual page

# File creation & deletion
touch file.txt              # create file
mkdir folder                # create directory
rm file                     # remove file
rm -r folder                # remove directory recursively

# Copying & moving
cp src dest                 # copy file
mv old new                  # move or rename file

# File type
file filename               # determine actual file type

# Permissions
ls -l                       # view permissions and metadata

```

---

# What I Learnt
- SSH is the standard way to interact with remote Linux systems securely.
- `man` pages are the most reliable source of command documentation.
- Linux permissions follow a consistent structure that becomes intuitive with practice.
- `rm -r` is powerful but dangerous—double-check paths before running it.
- File extensions are optional; Linux cares about content, not names
