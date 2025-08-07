#TCP Port Scanner for Local Network 7/12/25 Parker St. Julian  

#Used to create sockets that listen or establish connections on a network
import socket

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


#Creating a socket for the scanner that uses IPv4 adresses and uses TCP connections.
#A socket is essentially a virtual connection point that can listen for and establish connections within a network.
#In this python code, it is an object that abstracts lower-level networking functiions within your operating system.
#I used to think of sockets and ports being the same because I thought of them to be endpoints for connections, but a socket is an actual mechinism that makes connections, while a port is just a number that further identifies what aplication on a machine is providing a service.
scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Were establishing this behavior now so when the socket does try to use connect() in the future it will not hang on to closed or filtered ports for lomger than 1 second instead of several seconds.
scanner_socket.settimeout(1)

#Test port
port = 80

#This statement will try to connect to the targets IP and port, if it works, it will display the first messages, if it doesnt, which means the port is either closed or filtered, then it will display the second, and lastly, wether it connects or not, it will close the socket, essesntially endind the connection.
#connect() accepts one argument, so in order for us to send the target IP and port as one argument, we group it as one. (target_ip,port).
try:
    scanner_socket.connect((target_ip,port))
    print(f"\n[+] Port {port} is open")
except:
    print(f"\n[-] Port {port} is closed or filtered")
finally:
    scanner_socket.close()
