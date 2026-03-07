# JavaScript Essentials

**Path:** Cyber Security 101 > Web Hacking 

**Date Completed:** Jan 22, 2026  

**Difficulty:** Easy

---

## Summary
This room introduces JavaScript as an interpreted, client-side language and explores its role in web security. It focuses on how JS can be manipulated via the browser console to bypass local validation and how obfuscation is used to hide malicious intent.

---

## Key Concepts
* JS runs line-by-line in the browser engine (e.g., V8) and can be internal (within `<script>` tags) or external (linked files).
* A common architectural flaw where security checks (like password length or admin status) are performed in JS, making them trivial to bypass.
* Minification reduces file size by stripping whitespace, while Obfuscation intentionally hides logic using hex codes or complex formatting.

---

## Commands & Tools

### Variable Declaration & Types
```javascript
// Block-scoped declarations
let mutableValue = "can change";
const fixedValue = "cannot be reassigned";

// Data Types
let user = {name: "admin", id: 1}; // Object
let flags = ["user", "root"];      // Array
```
### Dialogue Functions (XSS PoC)
```javascript
alert("XSS Found");        // Simple OK box; standard PoC
prompt("Enter Password");   // Returns user input or null
confirm("Are you sure?");   // Returns true or false
```

---

# What I Learned

- Any security logic written in JS can be bypassed by the user; true authorization must happen on the server.
- You can manually override logic in the Developer Console; for example, changing if (password == "admin") to if (true) instantly grants access to local-only features.
- Attackers often hide sensitive or malicious logic in external .js files, assuming users will only check the main HTML source.
- Always grep/search JS files for API keys, hardcoded passwords, or developer-only endpoints that were mistakenly left in the production code.
- Successfully triggering an alert() through a user-input field is the universal proof that a site is vulnerable to Cross-Site Scripting (XSS)
