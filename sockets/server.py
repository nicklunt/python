#!/usr/bin/env python3

'''
CREDIT: https://www.youtube.com/watch?v=3QiPPX-KeSc
'''

import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    print(f"[{addr}] disconnected")
    conn.close()

# Wait for incoming connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR[0]}:{ADDR[1]}")
    while True:
        # conn = client object we can send data to
        # addr = client ip addr and port etc
        conn, addr = server.accept() # waits here for a connection

        # When we get a connection send it to handle_client()
        # Start a thread so multiple clients can connect without one client blocking another
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

print("[STARTING] server is starting")
start()



