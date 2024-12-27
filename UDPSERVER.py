from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('localhost',serverPort))
print("The server is ready to receive")
while 1:
    message,clientAddress=serverSocket.recvfrom(2048)
    print(f"A connection is made with {clientAddress}")
    modifiedMessage=message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)