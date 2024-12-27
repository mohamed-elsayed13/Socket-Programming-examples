import socket
URL =input("Enter the URL : ") #Ex: 127.0.0.1:12345/hello.html
split1=URL.split(':')
split2=split1[1].split('/')
serverIP=split1[0]
serverPort=int(split2[0])
filePath=split2[1]
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
request=f"GET /{filePath} HTTP/1.1\r\n"
clientSocket.send(request.encode())
content=""
response = clientSocket.recv(2048)
while response:
    content += response.decode()
    response = clientSocket.recv(2048)
print(content)    