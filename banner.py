import socket
import sys

def banner_grabbing(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target, port))
        banner = s.recv(1024)
        return banner.decode() .strip()
    except Exception as e:
        return str(e)
    finally:
        s.close()

if __name__ == "__main__":
    target = sys.argv[1]
    a = socket.gethostbyname(target)
    port = 22
    print(f"Banner from {a}:{port} - {banner_grabbing(a, port)}")