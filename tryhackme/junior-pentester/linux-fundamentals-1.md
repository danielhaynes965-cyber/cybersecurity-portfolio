# Linux Fundamentals 1
**Path:** Cyber Security 101 > Linux Fundamentals
**Date Completed:** Nov 29, 2025
**Difficulty:** Easy

---

## Summary
This room introduces the absolute basics of interacting with a Linux system through the terminal. It focuses on navigation, essential commands, searching for files, and understanding shell operators. These fundamentals matter because much cybersecurity work relies on being comfortable and efficient in a Linux CLI environment.

---

## Key Concepts
- Linux commands follow a predictable structure: *command* + *options* + *arguments*
- Navigating the filesystem is like learning to walk; nothing exciting but still crucial to all operation
- Searching/filtering information quickly is esential for real-world tasks
- Shell operators allow chaining, redirecting, and backgrounding tasks

---

## Commands & Tools
```bash
# Identity & output
whoami                # show current user
echo "text"           # print text or variables

# Navigation
ls                    # list files
cd folder             # move into folder
cd ..                 # go up one directory
pwd                   # show full path
cat file.txt          # print file contents

# Searching
find -name "*.txt"    # search for files by name/pattern
grep "value" file     # search inside files

# Shell operators
command &             # run in background
cmd1 && cmd2          # run cmd2 only if cmd1 succeeds
echo "text" > file    # overwrite file
echo "text" >> file   # append to file

```

---

## What I Learned
- Using basic naviagation commands becomes second nature quickly
- The CLI facilitates advances navigation too; it get's a lot more complicated and sophisticated
