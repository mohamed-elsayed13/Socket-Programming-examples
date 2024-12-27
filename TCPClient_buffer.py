import socket
HEADERSIZE = 10 #used to contain the length of actual msg
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1241))
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16) #read upto 16 bytes at a time
        if new_msg:
            #extracts the first 10 bytes of the received data (slicing) which are the header
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")
        #message assembly (adds decoded chunks of msg until entire msg is received)
        full_msg += msg.decode("utf-8")
        print(f"recieved until now {full_msg}")
        print(f"length of message recieved until now {len(full_msg)}")

        '''
        prints the whole message when the 
        length of the received message (len(full_msg)-HEADERSIZE) 
        equals the (msglen) taken from the header
        '''
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True