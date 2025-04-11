import socket
import psutil

def get_used_ports():
    used_ports = set()
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN' and conn.laddr:
            used_ports.add(conn.laddr.port)
    return sorted(used_ports)

if __name__ == "__main__":
    ports = get_used_ports()
    print("🔍 Ports currently in use:")
    for p in ports:
        print(f" - Port {p}")
