import socket
import pickle
'''
pickle module is used to serialize and deserialize large data into bytes 
EX:functions, giant dictionaries, arrays, a TensorFlow model.
'''
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    #declare a tuple to send
    d = (1,2,3,4)
    msg = pickle.dumps(d) #converts the tuple to bytes(serializing)
    #add the header to the serialized data that will be sent
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)