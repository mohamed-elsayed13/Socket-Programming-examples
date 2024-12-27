import socket
from threading import Thread # To handle each client request in a separate thread.
from time import ctime # To display the current time when a thread starts
from time import sleep  # Import the sleep function

def serviceRequest(clientConnection):
    print(f"New Thread started on {ctime()}")
     # Add a delay of 5 seconds
    sleep(5)
    try:
        request= clientConnection.recv(2048)
        print(request.decode())
        filename=request.split()[1]
        f=open(filename[1:])
        outputData=f.read()
        # Header to be sent 200 Ok 
        header ="HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        clientConnection.send(header.encode())
        for i in range(0,len(outputData)):
            clientConnection.send(outputData[i].encode())
        clientConnection.close()
    except IOError:
        # Header to be sent 404 file not found 
        header ="HTTP/1.1 404 Not Found\r\n"
        clientConnection.send(header.encode())
        clientConnection.close()

serverIP = '127.0.0.1'
serverPort = 12345
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((serverIP,serverPort))
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.listen(40)
threads=[]
while True:
    clientConnection , clientAddr = serverSocket.accept()
    print(f"Conection Established with client = {clientAddr}")
    newThread=Thread(target=serviceRequest,args=(clientConnection,))
    newThread.start()
    threads.append(newThread)
serverSocket.close()    