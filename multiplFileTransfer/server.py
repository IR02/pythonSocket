import socket

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

        msg = conn.recv(SIZE).decode(FORMAT)
        print(msg)

def main():
    print("[STARTING] Server is starting ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start(server)

if __name__ == "__main__":
    main()
