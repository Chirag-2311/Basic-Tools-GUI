from scapy.all import *
import socket
import sys

def packet(count):
    pack = ""
    packets = sniff(count = count)
    for packet in packets:
        pack += str(packet) + "\n"
    return pack

if __name__ == "__main__":
    a = sys.argv[1]
    print(packet(a))