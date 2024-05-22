import socket
import os

# Constants
PORT = 4455
SERVER = socket.gethostbyname(socket.gethostname())
SIZE = 1024
FORMAT = 'utf-8'
CLIENT_FOLDER = "client_folder"

def main():

    # Start socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print(f"[CONNECTED] Connected to the server at {SERVER}:{PORT}")

    # msg = "Hello Server!!"
    # client.send(msg.encode(FORMAT))
    # client.close()
    # print("[DISCONNECTED] Disconnected from the server")

    # Folder path
    path = os.path.join(CLIENT_FOLDER, "files")
    folder_name = path.split("/")[-1]
    
    # Send the folder name
    msg = f"{folder_name}"
    print(f"[CLIENT] Sending folder name: {folder_name}")
    client.send(msg.encode(FORMAT))

    # Receive reply from serveer
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {msg}\n")

if __name__ == "__main__":
    main()
