import socket
LISTEN_PORT = 5555
print()
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
msg = "key"
client_soc.sendall(msg.encode())
client_msg = client_soc.recv(1024)
client_msg = client_msg.decode()

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
msg = client_msg
sock.sendall(msg.encode())
print("message sent to server was: "+msg)
