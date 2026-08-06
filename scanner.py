import socket

target = input("Enter target IP or domain: ")
ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
                if banner:
                    print(f"    Banner: {banner}")
            except:
                print("    No banner received")
        s.close()
    except Exception as e:
        print(f"Error on port {port}: {e}")

print("\nScan completed.")