# Simple UDP server to convert text to upper-case
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server is ready on port", serverPort)
while 1:
     message, clientAddress = serverSocket.recvfrom(2048)
     print("... received message from", clientAddress[0])
     modifiedMessage = bytes.decode(message).upper()
     serverSocket.sendto(str.encode(modifiedMessage), clientAddress)
      
