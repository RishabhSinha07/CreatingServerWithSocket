import socket

PORT = 6000
HEADER = 64  # Bytes, Size of the msg
FORMAT = 'UTF-8'
DISCONNECT_MSG = "!disconnect"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)  # Encode str to bytes like obj to send
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)


send("Hello")
send("Testing success")
send(DISCONNECT_MSG)
