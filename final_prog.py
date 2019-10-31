# connect via terminal
#telnet localhost 10000

import datetime
from socket import socket

x = datetime.datetime.now()
my_time = x.strftime("%c")
print (my_time)
s = socket() # create object
try:
    s.bind(('0.0.0.0',10000)) # all IP address allowed, on PORT 10000
    print("Server started")
    s.listen(5)
    sock, address = s.accept()
    print("Connection established with ", address)
    sock.send(b'Welcome to server.\n')
    sock.send(my_time.encode())
    sock.send(b'\n')
    while True:
        line = sock.recv(8195)
        if line.strip()==b'data':
            sock.send(b"Here is the data:\n")
            with open('cfg.txt') as file:
                sock.send(file.read().encode())
                sock.send(b"\n")
        elif line.strip()==b'exit':
            break
        else:
            sock.send(b"Incorrect command.\n")
            sock.send(b"Type 'data' to retrieve data.\nType 'exit' to exit.\n") 
    
except:
    print("*Error has occurred.*")
finally:
    sock.close()
    s.close()
    print("Connection terminated")


