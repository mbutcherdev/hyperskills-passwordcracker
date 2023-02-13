# Create a connection, send the cli args

import socket
import sys


def create_connection(host_address, port, message):
    with socket.socket() as new_conn:
        new_conn.connect((host_address, port))
        new_conn.send(message.encode())
        print(new_conn.recv(1024).decode())


host_address = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

create_connection(host_address, port, message)
