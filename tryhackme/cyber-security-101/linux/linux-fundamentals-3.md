# Linux Fundamentals 3

**Path:** Cyber Security 101 > Linux Fundamentals

**Date Completed:** Nov 30, 2025

**Difficulty:** Easy

---

# Summary
This room introduces text editors, downloading/serving files, process management, automation with cron, and package management. These skills matter because they form the backbone of real system administration and are used constantly in penetration testing and CTF environments.

---

# Key Concepts
- Text editors like nano and vim are essential for modifying configuration files.
- Linux can download, serve, and transfer files using built‑in tools.
- Processes and services can be monitored and controlled directly from the terminal.
- Cron jobs automate repetitive tasks.
- APT manages software installation and updates on Debian-based systems.

---

# Commands & Tools
```bash
# Text editors
nano file.txt              # beginner-friendly editor
vim file.txt               # advanced editor

# Downloading & transferring
wget http://IP/file        # download file
scp src dest               # secure copy over SSH

# Serving files
python3 -m http.server     # simple web server on port 8000

# Processes
ps                         # processes for current session
ps aux                     # all processes
top                        # real-time process monitor
kill PID                   # terminate process (SIGTERM)
kill -9 PID                # force kill (SIGKILL)

# Services
systemctl status service   # check service status
systemctl start service    # start service
systemctl stop service     # stop service
systemctl enable service   # run on boot

# Cron
crontab -e                 # edit cron jobs
# minute hour day month weekday command

# Package management
apt update                 # refresh package lists
apt install package        # install software

# Logs
ls /var/log                # view log directory

```

---

# What I Learnt
- `nano` is great for quick edits, but learning vim pays off long-term.
- Python’s built-in web server is perfect for quick file transfers in labs.
- Understanding signals (`SIGTERM` vs `SIGKILL`) helps avoid breaking processes.
- Cron syntax looks intimidating but is predictable once broken into fields.
- System logs in `/var/log` are invaluable for troubleshooting and investigations.
