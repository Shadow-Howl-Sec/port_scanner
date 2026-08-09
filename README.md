# 🔍 Port Scanner

A fast, multi-threaded Python port scanner with banner grabbing — scan any IP or domain for open ports in seconds.

## Features

- ⚡ **Multi-threaded scanning** — uses `ThreadPoolExecutor` for fast concurrent scans
- 🎯 **Custom port input** — specify your own ports or use the built-in default list
- 🏷️ **Banner grabbing** — sends an HTTP request and captures service banners on open ports
- 📄 **Results logging** — saves scan results to `open_ports.txt` automatically
- 🕒 **Scan timer** — reports total scan duration

## Default Ports Scanned

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 53   | DNS     |
| 80   | HTTP    |
| 110  | POP3    |
| 139  | NetBIOS |
| 443  | HTTPS   |
| 445  | SMB     |
| 3389 | RDP     |
| 8080 | HTTP-Alt|
| 8443 | HTTPS-Alt|

## Requirements

- Python 3.x (no external dependencies — standard library only)

## Usage

```bash
python scanner.py
```

You will be prompted:

```
Enter target IP or domain: 192.168.1.1
Enter the ports you want to scan(default ports if left empty):
```

- **Leave ports blank** → scans the default port list above
- **Enter custom ports** → comma-separated, e.g. `80,443,8080,3000`

### Example Output

```
Scanning 192.168.1.1 with multi-threading...

[+] Port 22 is OPEN
[+] Banner: SSH-2.0-OpenSSH_8.9
[+] Port 80 is OPEN
[+] Banner: HTTP/1.1 200 OK

Scan completed in 3.24 seconds.

Scan completed.
```

## Output File

Results are appended to `open_ports.txt` in the working directory:

```
Target: 192.168.1.1
Open Ports: [22, 80]
Scan completed in 3.24 seconds.
-------------------------
```

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**.  
Do **not** use this tool on systems you do not own or have explicit permission to scan.  
Unauthorized port scanning may be illegal in your jurisdiction.

## License

MIT License — feel free to use, modify, and distribute.
