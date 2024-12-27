from socket import *
serverPort =12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(5)
print('The server is ready to receive')
while 1:
    connectionSocket, addr =serverSocket.accept()
    print(f"Client address {addr}")
    sentence=connectionSocket.recv(2048)
    CapitalizedSentence=sentence.decode("utf-8").upper()
    connectionSocket.send(bytes(CapitalizedSentence,"utf-8"))
    connectionSocket.close()