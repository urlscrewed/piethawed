import socket

# TCP Client
# Paddysbub
# The code is to start up a quick TCPclient in doing so. The below code needs the connection alway succeed and client expecting connection 


target_host = "www.google.com"
target_port = 80

#Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET = use a IPv4

#connect the client
client.connect((target_host,target_port))

#send some data 
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data 
response = client.recv(4096)

print response


