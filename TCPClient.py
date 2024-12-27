from socket import *
serverName= 'localhost'
serverPort= 12000
clientSocket=socket(AF_INET,SOCK_STREAM)
#clientSocket.bind(('',4059))
clientSocket.connect((serverName,serverPort))
sentence=input("Input lower case sentence")
clientSocket.send(bytes(sentence,"utf-8"))
modifiedSentence=clientSocket.recv(2048)
print('Form Server:' , modifiedSentence.decode("utf-8"))
clientSocket.close()