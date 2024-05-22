import socket
import os

# Constants
PORT = 4455
SERVER = socket.gethostbyname(socket.gethostname())
SIZE = 1024
FORMAT = 'utf-8'
SERVER_FOLDER = "server_folder"

def start(server):
    server.bind((SERVER, PORT))
    server.listen()
    print("[LISTENING] Server is waiting for clients.")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.\n")

        # Receive folder_name from client
        folder_name = conn.recv(SIZE).decode(FORMAT)
        print(folder_name)

        # Create folder
        folder_path = os.path.join(SERVER_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            conn.send(f"Folder ({folder_name}) created".encode(FORMAT))
        else:
            conn.send(f"Folder ({folder_name}) already exists.".encode(FORMAT))
        
        # Receive files

        

        # msg = conn.recv(SIZE).decode(FORMAT)
        # print(msg)

def main():
    print("[STARTING] Server is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start(server)

if __name__ == "__main__":
    main()
