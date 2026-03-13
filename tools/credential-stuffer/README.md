# Credential Stuffer

### What the tool does

- This tool was built to automatically attempt logins from a list of leaked usernames and passwords over a TCP connection.

### What it was built for

- Tool was built on the 13th March, 2026 (the first tool I've built and uploaded to my repository)
- I built it to solve the 'Credential Stuffing' challenge as part of my participatoin in picoCTF 2026

### Usage instruction

- The tool accepts three arguments (exculding --help or -h)
	- -p or --port
	- -f or --file 
	- -H or --host
- All three are required, however --file and --host have default values of 'creds.txt' and 'crystal-peak.picoctf.net' respectively
- Example usage: python3 credential-stuffer.py -p 60001
- After executing, there is no more user input required and the program will run until the wordlist is empty or until a match is found
- Note that the logic for whether or not the input was successful may likely need altering if the tool is used on a different site
- Can cancel the tool using Ctrl+C

### Expected input format

- The file with the usernames and passwords must have the format 'username;password', one per line (see creds.txt)

### Ethical disclaimer

- As applies to all the content in this repository, this tool is for authorised CTF use only and should not be used in a context where permission is not explicitely granted



