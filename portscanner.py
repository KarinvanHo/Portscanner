import socket
import termcolor


def scan(target, ports):
	print(f"'\nStarting Scan For {target}")
	for port in range(1, ports):
		scan_port(target, port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(f"[+] Port Opened {port}")
		sock.close()
	except TimeoutError:
		print("[x] No Response")
	except ConnectionRefusedError:
		pass


targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You want To Scan: "))


if ',' in targets:
	print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)

