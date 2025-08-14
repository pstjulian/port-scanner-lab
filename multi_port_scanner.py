#TCP Port Scanner for Local Network 7/12/25 Parker St. Julian  

#Used to create sockets that listen or establish connections on a network
import socket

#Used to track how long scans will take
from datetime import datetime


#This accepts a user input, which should be the target devices local IP address or hostname, like google.com, and stores it in the target variable.
target = input("\nEnter the local IP address or hostname to scan: ")

try:
    #If the hostname, like google.com, is used as the input instead of the IP, socket.gethostbyname() will resolve the hostname into an IP adress we can use.
    #If the an IP is used as an input, it will do nothing but return the IP again.
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    #Used error handling here to check if the hostname could be resolved into an IP or not.
    #This makes it easier to figure out where something went wrong if something does go wrong in the program.
    print("\nClould not resolve hostname.")
    exit()

print(f"\nStarting scan on target: {target_ip}")


# Track when the scan starts
start_time = datetime.now()

# Define the range of ports to scan
for port in range(1, 1024):  # You can increase this range if you'd like

    
    #Creating a socket for the scanner that uses IPv4 adresses and uses TCP connections.
    #A socket is essentially a virtual connection point that can listen for and establish connections within a network.
    #In this python code, it is an object that abstracts lower-level networking functiions within your operating system.
    #I used to think of sockets and ports being the same because I thought of them to be endpoints for connections, but a socket is an actual mechinism that makes connections, while a port is just a number that further identifies what aplication on a machine is providing a service.
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Were establishing this behavior now so when the socket does try to use connect() in the future it will not hang on to closed or filtered ports for lomger than 1 second instead of several seconds.
    scanner_socket.settimeout(0.5)


    try:
        #connect_ex() tries to connect the socket. The "ex" portions stands for extended error handling, so it will return a 0 if the connections is a success, and a non-zero value if it fails.
        #This avoids us from having to use the try/except block every single time we check a port.
        result = scanner_socket.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is open")
    except:
        pass  # Ignore errors and continue scanning
    finally:
        scanner_socket.close()

#Takes account for the time at the end of the scan, and compares it to the start time to find the total time it took to scan all ports.
#We then take the calculated time and print it out.
end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
