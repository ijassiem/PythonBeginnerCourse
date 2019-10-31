from socket import socket

sock = socket()

sock.connect(('localhost', 10000))

#sock.send(b'Good day mate')

print(sock.recv(8192))

sock.close() # close socket

