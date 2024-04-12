import scapy.all as scapy
import re
import sys
import socket

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
	ip_add_range_entered = sys.argv[1]
	if ip_add_range_pattern.search(ip_add_range_entered):
		print(f"{ip_add_range_entered} is a valid IP address range")
		break

#perform ARPing
arp_result=scapy.arping(ip_add_range_entered, verbose=False)[0]

#display results with hostnames
for sent, recieved in arp_result:
	ip=recieved.psrc
	mac=recieved.hwsrc
	try:
		hostname, _, _=socket.gethostbyaddr(ip)
	except socket.herror:
		hostname="Unknown"
	print(f"IP: {ip} MAC: {mac} Hostname: {hostname}")
	