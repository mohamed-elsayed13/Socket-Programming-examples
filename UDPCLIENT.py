from socket import *
serverName= 'localhost'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('input lower case sentense: ')
clientSocket.sendto(bytes(message,"utf-8"),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()