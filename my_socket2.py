from socket import socket

server_socket = socket()
try:
    server_socket.bind(('0.0.0.0',10000))
    server_socket.listen(5)
    sock, address = server_socket.accept()
    sock.send(b'Welcome to the dark web\n')
    sock.close()
finally:
    server_socket.close()

# connect via terminal
#telnet localhost 10000
