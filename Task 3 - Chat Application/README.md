# Task 3 - Chat Application

## Objective

The objective of this task was to build a real-time two-user chat application in Python using socket programming and threading.

## Features

- Supports communication between two clients.
- Uses TCP socket communication.
- Allows clients to connect through a local server.
- Supports sending and receiving messages in real time.
- Displays the sender's name with each message.
- Adds timestamps to messages.
- Handles client disconnection.
- Provides an exit option for the client.

## Technologies Used

- Python
- Socket Programming
- Threading
- TCP/IP
- Datetime

## Implementation

The application consists of a server and a client.

The server listens for incoming client connections and manages connected clients. When a client sends a message, the server broadcasts the message to the other connected client.

Threading is used on the client side so that messages can be received while the user can continue typing and sending messages.

The application was tested using two clients connected to the local server.

## Outcome

A functional real-time two-user chat application was successfully developed and tested. The application allows clients to connect, exchange messages, display timestamps, and disconnect safely.
