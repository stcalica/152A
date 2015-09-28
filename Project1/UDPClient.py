# Simple UDP client to send text to the server
from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Enter message: ")
clientSocket.sendto(str.encode(message),(serverName,serverPort));
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Server responded:", bytes.decode(modifiedMessage))
clientSocket.close();
