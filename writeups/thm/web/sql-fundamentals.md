# SQL Fundamentals

**Path:** Cyber Security 101 > Web Hacking

**Date Completed:** Jan 23, 2026  

**Difficulty:** Easy

---

## Summary
This room covers the basics of Relational Database Management Systems (RDBMS) and the Structured Query Language (SQL) used to interact with them. It details how data is organized into tables and how CRUD operations form the basis for web application functionality and potential injection vulnerabilities.

---

## Key Concepts
* Data is stored in structured tables consisting of **Columns** (attributes) and **Rows** (records).
* **Primary Keys** uniquely identify a record, while **Foreign Keys** link records across different tables to create relationships.
* **Data Definition (DDL)** are commands like `CREATE`, `DESCRIBE`, and `DROP` that manage the skeleton/structure of the database itself.
* **Data Manipulation (DML)** are "CRUD" cycle (Create, Read, Update, Delete) used to manage the actual information stored within those structures.

---

## Commands & Tools

### Structure Management (DDL)
```sql
SHOW DATABASES;                -- List all databases on the server
USE database_name;             -- Select a database to work in
SHOW TABLES;                   -- List all tables in the current DB
DESCRIBE table_name;           -- View column names and data types
```
### Data Operation (CRUD)
```sql
-- READ: Retrieve data (Most common for SQLi)
SELECT * FROM users WHERE username = 'admin';

-- CREATE: Add new records
INSERT INTO users (username, password) VALUES ('attacker', 'pass123');

-- UPDATE: Modify existing records (Requires WHERE clause)
UPDATE users SET password = 'pwned' WHERE id = 1;

-- DELETE: Remove records (Requires WHERE clause)
DELETE FROM users WHERE username = 'bob';
```
### Filtering & Pattern Matching
```sql
-- Logical Filtering
SELECT * FROM products WHERE price > 50 AND category = 'tech';

-- Pattern Matching (LIKE)
SELECT * FROM users WHERE username LIKE 'a%';      -- Starts with 'a'
SELECT * FROM users WHERE username LIKE '%admin%'; -- Contains 'admin'

-- Sorting & Limits
SELECT * FROM users ORDER BY id DESC LIMIT 3;      -- Newest 3 users
```

---

## What I Learned
- When performing UPDATE or DELETE operations, omitting the WHERE clause applies the change to every single row in the table—a common mistake that leads to massive data loss.
- SQL Injection works by manipulating the logic of a query (e.g., using OR 1=1) to trick the database into executing unintended commands, such as bypassing authentication.
- The % wildcard in a LIKE statement is a powerful tool for finding specific data strings when you only have partial information.
- In a CTF, DESCRIBE is a vital command for understanding the backend schema before attempting complex joins or exfiltration.
- Security via Abstraction: Real security comes from the server-side handling of these queries; user input should never be directly concatenated into the SQL string.
 
