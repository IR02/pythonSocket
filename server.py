import socket
import threading

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print(SERVER)

#CREATE SOCKET
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#BIND SOCKET to ADDRESS
server.bind(ADDR)

#HANDLE EACH CONNECTION
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
        
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{ADDR}] {msg}")
            conn.send("MSG received.".encode(FORMAT))
            
    conn.close()

       


#HANDLE NEW CONNECTION
def start():
    server.listen()
    print(f"[LISTENING] Server is listenong on {SERVER}")
    while True:
        #New connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args= (conn, addr))
        thread.start()
        #Active connection
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") 


print("[STARTING] server is starting...")
start()
