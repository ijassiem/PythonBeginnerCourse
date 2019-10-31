from socket import socket

sock = socket()

sock.connect(('www.ledge.co.za', 80))

sock.send(b'GET /\nHTTP/1.0\n\n\n')

print(sock.recv(8192))

sock.close() # close socket

sock = socket()

sock.connect(('www.ledge.co.za',25))

sock.send('ehlo 242-39-24-196.kat.ac.za.')

sock.recv(
