import socket
import pickle

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))
while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        print(f"full message length: {msglen}")
        full_msg += msg
        print(f"length of message recieved until now {len(full_msg)}")
        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            #prints only the pickled message excluding the header size
            print(full_msg[HEADERSIZE:])
            recvd_tuple = pickle.loads(full_msg[HEADERSIZE:])
            print(recvd_tuple)
            for i in recvd_tuple:
                print(i)
            new_msg = True
            full_msg = b''

