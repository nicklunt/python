#!/usr/bin/env python3

'''
CREDIT: https://www.youtube.com/watch?v=3QiPPX-KeSc
'''

import socket

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.30"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# send data to the server
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    # Has the server sent anything back        
    print(client.recv(2048).decode(FORMAT))

    # print(message)

send("Hello World!")
send("Nearly Christmas..")
send("Time for a Kebab :)")
send(DISCONNECT_MESSAGE)