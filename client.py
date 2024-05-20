import socket
import pickle

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message_dict):
    # Serialize the message using pickle
    message = pickle.dumps(message_dict)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    response = client.recv(2048)
    try:
        # Deserialize the response using pickle
        response_data = pickle.loads(response)
        print(f"[SERVER] {response_data}")
    except pickle.UnpicklingError as e:
        print(f"Error unpickling response: {e}")

# Send a dictionary message to the server
send({"message": "Hello Server!", "type": "greeting"})
input()
send({"message": "How are you?", "type": "question"})
input()
send({"message": DISCONNECT_MESSAGE, "type": "disconnect"})
