import socket

# Constants
PORT = 4455
SERVER = socket.gethostbyname(socket.gethostname())
SIZE = 1024
FORMAT = 'utf-8'
CLIENT_FOLDER = "client_folder"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"[CONNECTED] Connected to the server at {SERVER}:{PORT}")

    msg = "Hello Server!!"
    client.send(msg.encode(FORMAT))
    client.close()
    print("[DISCONNECTED] Disconnected from the server")

if __name__ == "__main__":
    main()
