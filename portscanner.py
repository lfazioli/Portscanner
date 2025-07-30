#!/usr/bin/env python3

import socket
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor
import ipaddress

host = input("Inserisci l'indirizzo IP: ")

try:
    ipaddress.ip_address(host)
except ValueError:
    print("Indirizzo IP non valido.")
    exit(1)

start_port = int(input("Porta iniziale: "))
end_port = int(input("Porta finale: "))

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(colored(f"[+] Porta {port} aperta", "green"))
        except:
            pass

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(start_port, end_port + 1))

if __name__ == "__main__":
    main()