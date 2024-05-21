import socket
import threading
import pickle
import signal
import sys

# Constants
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # Get the local machine name
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print(f"[STARTING] Server is starting on {SERVER}")

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
server.bind(ADDR)

# Function to handle shutdown signals
def signal_handler(sig, frame):
    print("\n[SHUTTING DOWN] Server is shutting down...")
    server.close()
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Function to handle shutdown signals
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive the message length header
        msg_length = conn.recv(HEADER).decode(FORMAT).strip()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            
            # Deserialize the message using pickle
            try:
                data = pickle.loads(msg)
                if data.get("message") == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {data}")
                
                # Send a response back to the client
                response = {"status": "success", "data": "Message received."}
                response_serialized = pickle.dumps(response)
                conn.send(response_serialized)
            except pickle.UnpicklingError as e:
                print(f"Error unpickling message: {e}")
            
    conn.close()

# Function to start the server and handle incoming connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Accept a new connection
        conn, addr = server.accept()
        # Start a new thread to handle the client connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Active connection
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start()
