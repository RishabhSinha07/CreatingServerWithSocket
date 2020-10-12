import socket
import threading

PORT = 6000
HEADER = 64  # Bytes, Size of the msg
FORMAT = 'UTF-8'
DISCONNECT_MSG = "!disconnect"
# ipconfig give local information not public ip address
# SERVER = " 192.168.56.1" but instead of hardcoading use the following line

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# socket.AF_INET tells the socket what kind of ip address we're getting or looking for
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bound this socket to this addr so anything that connect to this add will hit this socket
server.bind(ADDR)


def handle_client(conn, addr):
    # Will Run concurrently for each client
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        # will stay untill get the msg thats why threading
        # We will fisrt ask the size of the message and padd it to 65 bytes. Value 64 is small just for testing and when we get the size of the msg user that to define the listener
        msg_len = conn.recv(HEADER).decode(FORMAT)  # bytes -> string
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f"[{addr}]:{msg}")
            if msg == DISCONNECT_MSG:
                connected = False
                print("USER DISCONNECTED")
    conn.close()
    # Very important to disconnect user bcoz if user diss and tries to recc then the server will say we have the user already login and cannot allow


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Sub 1 for the listening thread
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")


print("[STARTING] server is starting...")
start()
