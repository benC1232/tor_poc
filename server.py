import socket



PORT: int = 8637

def main() -> None:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        #binding the scoket
        sock.bind(("",PORT))
        # Listen for incoming connections
        sock.listen(1)
        #Create a New Conv Socket
        while True:
            client_soc, client_addr = sock.accept()
            client_msg = client_soc.recv(1024).decode()
            print(client_msg)
