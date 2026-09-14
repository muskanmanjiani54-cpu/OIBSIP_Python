import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                pass

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(message)
            broadcast(message, client)

        except:
            break

    if client in clients:
        clients.remove(client)

    broadcast("A client has disconnected.", client)
    client.close()


print(f"Server started on {HOST}:{PORT}")
print("Waiting for clients...")

while True:
    client, address = server.accept()

    clients.append(client)

    print(f"Client connected: {address}")

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()