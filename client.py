import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to remote computer 80
server_address = (SERVER_IP, SERVER_PORT)
sock.connect(server_address)
server_msg = sock.recv(1024)
server_msg = server_msg.decode()
key = server_msg
msg = input()
sock.sendall(msg.encode())

