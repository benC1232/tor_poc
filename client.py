import rsa
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to remote computer 80
server_address = (SERVER_IP, SERVER_PORT)
sock.connect(server_address)
#recieveing keys of rsa
server_msg = sock.recv(1024)
decoded = str(server_msg, 'utf8')
n = int(decoded)
server_msg = sock.recv(1024)
decoded = str(server_msg, 'utf8')
e = int(decoded)
#getting message to send to server
msg = input("")
#encrypting message
publicKey = rsa.PublicKey(n, e)
encMessage = rsa.encrypt(msg.encode(), publicKey)
#sending message and closing the socket
sock.sendall(encMessage)
sock.close()
