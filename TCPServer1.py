#from socket import *
import socket
#serverIP = "127.0.0.1"
#serverIP = "localhost"
serverIP = "192.168.56.1"
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen()
print('The server is ready to receive')
while 1:
    connectionSocket, client_addr = serverSocket.accept()
    print(f"Client Address = {client_addr}")
    sentence = connectionSocket.recv(2048)
    print(f"Received {sentence}")
    capitalizedSentence = sentence.decode("utf-8").upper()
    connectionSocket.send(bytes(capitalizedSentence,"utf-8"))
    connectionSocket.close()