import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                print("\n" + message)
                print("You: ", end="")

        except:
            break



thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

print("Connected to chat!")
print("Type your message and press Enter.")
print("Type 'exit' to leave.\n")

while True:
    message = input("You: ").strip()

    if not message:
        continue

    if message.lower() == "exit":
        client.close()
        print("Disconnected from server.")
        break

    time = datetime.now().strftime("%H:%M")
    full_message = f"[{time}] {name}: {message}"

    try:
        client.send(full_message.encode())
    except:
        print("Connection lost.")
        break
