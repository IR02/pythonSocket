import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(SERVER)

#CREATE SOCKET
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#BIND SOCKET to ADDRESS
server.bind(ADDR)

#SOCKET LISTENING
def handle_client(conn, addr):
    pass

def start():
    pass

print("[STARTING] server is starting...")
start()
