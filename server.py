import socket
import threading
import pickle

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print(SERVER)

# Create sockeet
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
server.bind(ADDR)

# Handle eeach connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT).strip()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)

            # Deserialize the message using pickle
            try:
                data = pickle.loads(msg)
                if data == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {data}")
                
                # Sending a response
                response = "MSG received."
                response_serialized = pickle.dumps(response)
                conn.send(response_serialized)
            except pickle.UnpicklingError as e:
                print(f"Error unpickling message: {e}")
            
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
