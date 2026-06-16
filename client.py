import socket
from cryptography.fernet import Fernet

with open("secret.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket()
client.connect((HOST, PORT))

while True:
    msg = input("You: ")
    client.send(cipher.encrypt(msg.encode()))

    data = client.recv(4096)
    print("Server:", cipher.decrypt(data).decode())
