# Linux Shells

**Path:** Pre-Security > Command Line  

**Date Completed:** Dec 25, 2025

**Difficulty:** Easy

---

## Summary
This room explores the shell as the primary interface between the user and the Linux OS kernel. It covers the distinctions between popular shells like Bash, Zsh, and Fish, while introducing foundational Bash scripting for task automation.

---

## Key Concepts
- Shell acts as a command-line interpreter that translates user instructions into actions the kernel can execute.
- While Bash is the industry standard, Zsh offers better customization (Kali/macOS), and Fish prioritizes user-friendly features like auto-suggestions.
- Scripting allows for the logical execution of complex tasks using variables, loops, and conditional logic.
---

## Commands & Tools
```bash

# Identify the current shell environment
echo $SHELL

# Change the default login shell to Zsh
chsh -s /usr/bin/zsh

# View command history to audit past actions
history

# Search for specific strings within a file
grep "pattern" filename.txt

# Make a script executable
chmod +x script.sh

# Basic Scripting Structure (The Shebang)
#!/bin/bash

# Variable usage and User Input
NAME="Security_Analyst"
read -p "Enter target IP: " target

# Conditional Logic
if [ -f "/etc/passwd" ]; then
    echo "File exists."
fi

# Iteration
for user in root admin; do
    echo "Checking $user..."
done

```

---

## What I Learned
- Always start scripts with #!/bin/bash (or the relevant path) to ensure the correct interpreter handles the code.
- Checking /etc/shells is the quickest way to see which environments are safely available on a compromised or new system.
- In Bash, do not put spaces around the = when assigning variables (e.g., NAME="User"), or the shell will mistake the variable for a command.
- A script won't run as a program until chmod +x is applied; otherwise, you have to manually invoke it via bash script.sh..
 
---
