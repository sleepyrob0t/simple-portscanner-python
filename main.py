import socket # for connecting to the host 
from colorama import init, Fore

# adding some colors (optional)
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port):
    
    #determines whether the host has the port open
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make a timeout if you want it a little faster (means less accuracy)
        # s.settimeout(0.2) <-- if you want to add a timeout 
    except:
        # cannot connect (port is closed) and returns false 
        return False
    else:
        # the connection is established (port is open)
        return True


# asks user to enter a port 
host = input("Enter the host:")
# repeat over ports, from 1 to 1024
for port in range(1, 1024):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")   #prints green text for open ports 
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r") #prints gray text for closed ports 