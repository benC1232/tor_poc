import rsa
import socket

LISTEN_PORT = 5555
"""
recieving encrypted message from client
"""
# Create a TCP/IP socket
listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding to local port 80
server_address = ('', LISTEN_PORT)
listening_sock.bind(server_address)
# Listen for incoming connections
listening_sock.listen(1)
# Create a new conversation socket
client_soc, client_address = listening_sock.accept()
#generate keys for rsa
publicKey, privateKey = rsa.newkeys(512)
n = bytes(str(publicKey.n), 'utf-8')
e = bytes(str(publicKey.e), 'utf-8')
#send keys to client
client_soc.sendall(n)
client_soc.sendall(e)
#recieveing encrypted message
client_msg = client_soc.recv(1024)
client_msg = client_msg
#closing socket with client
listening_sock.close()
"""
sending message to server
"""

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8637
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to remote computer 80
server_address = (SERVER_IP, SERVER_PORT)
sock.connect(server_address)
#decrypting and sending message
decMessage = rsa.decrypt(client_msg, privateKey)
sock.sendall(decMessage)
print("message sent to proxy was: " + str(client_msg))
print("message sent to server was: " + str(decMessage))
sock.close()
