#!/usr/bin/env python3

import socket  # Importa il modulo socket per creare connessioni di rete
from termcolor import colored  # Importa termcolor per colorare l’output nel terminale
from concurrent.futures import ThreadPoolExecutor   # Importa il modulo per eseguire scansioni in parallelo
import ipaddress  # Importa il modulo per validare gli indirizzi IP

# Chiede all’utente l’indirizzo IP da scansionare
host = input("Inserisci l'indirizzo IP: ")

# Controlla che l’indirizzo IP inserito sia valido
try:
    ipaddress.ip_address(host)  # Verifica se l'IP inserito è nel formato corretto (IPv4 o IPv6)
except ValueError:
    print("Indirizzo IP non valido.")  # Se non è valido, stampa un messaggio di errore
    exit(1)  # Termina l’esecuzione del programma

# Chiede all’utente l’intervallo di porte da scansionare
start_port = int(input("Porta iniziale: "))  # Porta di partenza per la scansione
end_port = int(input("Porta finale: "))  # Porta finale per la scansione

# Funzione che scansiona una singola porta
def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Crea un socket IPv4 con protocollo TCP
        s.settimeout(1)  # Imposta un timeout di 1 secondo per evitare blocchi su porte chiuse
        try:
            s.connect((host, port))  # Prova a connettersi alla porta sul target
            print(colored(f"[+] Porta {port} aperta", "green"))  # Se la connessione riesce, la porta è aperta
        except:
            pass  # Se c’è un errore (es. porta chiusa), non fa nulla e passa alla successiva

# Funzione principale del programma
def main():
    with ThreadPoolExecutor(max_workers=100) as executor:  # Crea un pool di 100 thread per scansionare più porte in parallelo
        executor.map(scan_port, range(start_port, end_port + 1))  # Assegna ogni porta da scansionare a un thread

# Controlla che il programma venga eseguito direttamente (non importato come modulo)
if __name__ == "__main__":
    main()  # Avvia il programma
# Fine del codice