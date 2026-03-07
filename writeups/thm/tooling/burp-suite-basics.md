# Burp Suite: The Basics

**Path:** Cyber Security 101 > Web Hacking  

**Date Completed:** Jan 24, 2026  

**Difficulty:** Easy

---

## Summary
Burp Suite is an essential intercepting proxy framework used to analyze and manipulate traffic between a web browser and a server. By acting as a Man-in-the-Middle (MITM), it allows researchers to modify requests in real-time, automate brute-force attacks, and decode various data formats.

---

## Key Concepts
* Browser → Burp (Hold/Edit) → Server → Burp (Capture) → Browser.
* **The "Big Three" Tools:**
    * **Proxy:** Real-time interception and traffic logging.
    * **Repeater:** Manual modification and re-sending of individual requests.
    * **Intruder:** Automated fuzzing and brute-forcing using defined payload positions.

---

## Commands & Tools

### Essential Shortcuts
| Shortcut | Action |
| :--- | :--- |
| **CTRL + R** | Send current request to **Repeater** |
| **CTRL + I** | Send current request to **Intruder** |
| **CTRL + T** | Toggle **Intercept** On/Off |
| **CTRL + F** | **Forward** the intercepted request |

### Utility Modules
* **Decoder:** Manually or "Smart" decode Base64, URL, Hex, and more.
* **Comparer:** Visual diff tool to find subtle changes between two responses.
* **Sequencer:** Analyzes the entropy (randomness) of session tokens.

---

## What I Learned
* Repeater is the most used tool for testing injections (SQLi, XSS) because it allows you to change a single character and see the response immediately without a page refresh.
* Even if Intercept is "Off," all traffic is logged in the **HTTP History** tab; you can always go back and send an old request to Repeater later.
* Using the **Target > Scope** feature filters out background noise (like Windows or browser updates), allowing you to focus strictly on the CTF target IP.
* The **Render** tab in Repeater is highly useful for visualizing HTML responses to see if payloads (like XSS) actually modified the page layout.
* Use the in built browser for HTTPS testing to avoid downloading the certificate.

---

## References
- [PortSwigger Academy: Burp Suite Documentation](https://portswigger.net/burp/documentation)
