import socket
from concurrent.futures import ThreadPoolExecutor
import time

target = input("Enter target IP or domain: ")
ports_default = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389, 8080, 8443]
ports = input("Enter the ports you want to scan(default ports if left empty): ")
if not ports:
    ports = ports_default
else:
    ports = ports.split(",")
    ports = [int(port) for port in ports]

open_ports = []
starttime = time.time()
def scan_port(port):
    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            s.send(("GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n").encode())
            banner = s.recv(1024).decode(errors="ignore").strip()
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN")
            if banner:
                print(f"[+] Banner: {banner}")
        s.close()
    except :
        pass

print(f"\nScanning {target} with multi-threading...\n")

with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scan_port, ports)


endtime = time.time()
with open("open_ports.txt", "a") as f:
    f.write(f"Target: {target}\n")
    f.write(f"Open Ports: {open_ports}\n")
    f.write(f"Scan completed in {endtime - starttime} seconds.")
    f.write("\n-------------------------\n")

print(f"Scan completed in {endtime - starttime} seconds.")
print("\nScan completed.")