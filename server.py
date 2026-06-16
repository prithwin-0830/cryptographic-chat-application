import socket
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(4096)
    if not data:
        break

    print("Client:", cipher.decrypt(data).decode())

    msg = input("You: ")
    conn.send(cipher.encrypt(msg.encode()))

conn.close()
server.close()
