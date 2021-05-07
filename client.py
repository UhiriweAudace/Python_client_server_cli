#!/usr/bin/env python3
"""
Add header to client message
"""
import socket
import sys
from options_controller import receive_message, chunking_and_send_message, load_arguments_options


def run_main_client(arguments):
    """This method spin up the client side
    """
    host = socket.gethostbyname(socket.gethostname())
    port = 65452

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
    except ConnectionRefusedError:
        print("Sorry Server is down")
        sys.exit(0)

    print("Connecting to the server....")
    print(str(f"Trying to connect to {host}:{port}\n"))

    buffer_size_msg = connection.recv(1024)
    buffer_size_msg = buffer_size_msg.decode()
    server_buffer_size = buffer_size_msg.split(':')
    server_buffer_size = int(server_buffer_size[1])
    print("Server Buffer Size : ", server_buffer_size)

    # Check if the server buffer size is equal to the client buffer size
    if server_buffer_size != arguments.packet_size:
        print('Oops, your buffer size is not equal to the server buffer size')
        sys.exit(0)

    msg_count = 1
    while True:
        input_message = input("Me: ")
        # Quit the application if user entered quit message
        if input_message == "quit":
            input_message = "You left chat room!"
            print(f"{input_message}\n")
            sys.exit(0)

        # Chunking the original message into multiple part based the provided buffer size
        chunking_and_send_message(connection, msg_count, input_message, arguments.packet_size)

        # Wait and receive the message from the Server
        server_msg = receive_message(connection, msg_count, server_buffer_size)
        print("Server: ", server_msg)
        msg_count += 1


if __name__ == "__main__":
    ARGUMENTS = load_arguments_options()
    run_main_client(ARGUMENTS)
