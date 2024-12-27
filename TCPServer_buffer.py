import socket
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1241))
s.listen(5)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    msg = "Welcome to the server!"
    #prepending the the message with the header size that contains the length of the data sent
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    print("sending ",{bytes(msg,"utf-8")})
    clientsocket.send(bytes(msg,"utf-8"))