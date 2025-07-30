# Python Port Scanner

A simple multithreaded port scanner written in Python 3. This tool allows you to scan a range of ports on a specified IP address to identify which ports are open.

## Features

- Input validation for IP addresses
- Fast scanning using multithreading (ThreadPoolExecutor)
- Colored output using `termcolor`
- Customizable port range

## Requirements

- Python 3.x
- `termcolor` module

Install dependencies with:

```bash
pip install termcolor
```

## Usage

Run the script with:

```bash
python3 portscanner.py
```

You will be prompted to enter:

- An IP address to scan
- A starting port
- An ending port

### Example

```bash
$ python3 portscanner.py
Enter the IP address: 192.168.1.1
Start port: 20
End port: 100

[+] Port 22 open
[+] Port 80 open
```

## How It Works

- Validates the IP address format using the `ipaddress` module
- Uses a thread pool to scan ports concurrently
- Tries to establish a TCP connection to each port
- If the connection is successful, the port is considered open

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Unauthorized port scanning is illegal and unethical.

