from socket import *
serverIP = "192.168.56.1"
#serverIP = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(bytes(sentence,"utf-8"))
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode("utf-8"))
clientSocket.close()
