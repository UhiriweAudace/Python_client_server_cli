
"""import required libraries"""
import sys
import platform
from datetime import datetime


def print_device_information():
    """This method will print out the device system information"""
    print("\nServer System information")
    print("----------------------------")
    print(f"platform detail : {platform.platform()}")
    print(f"system name : {platform.system()}")
    print(f"processor name : {platform.processor()}")
    print(f"architectural detail : {platform.architecture()}")
    sys.exit(1)


def print_current_time():
    """This method will print out the current date and time on the server which is up running"""
    print('Current Date and Time is ', datetime.now())
    sys.exit(1)


def receive_message(connection, msg_count, buffer_size):
    """This method handles received messages"""
    server_message = ""
    while True:
        final_buffer_size = buffer_size+2
        server_received_msg = connection.recv(final_buffer_size)
        splitted_msg = server_received_msg.decode().split('|')
        server_message += splitted_msg[0]
        try:
            if msg_count == int(splitted_msg[1]):
                continue
        except IndexError:
            break
    return server_message


def chunking_and_send_message(connection, msg_count, input_message, client_buffer_size):
    """This method chunks the sent message and send it"""
    message = str(input_message)
    message_parts = [message[i:i+client_buffer_size]
                     for i in range(0, len(message), client_buffer_size)]

    for index, msg_text in enumerate(message_parts):
        final_part_msg = ''
        if message_parts[index] != message_parts[len(message_parts) - 1]:
            final_part_msg = str(f'{msg_text}|{msg_count}')
        else:
            final_part_msg = str(f'{msg_text}')
        connection.send(final_part_msg.encode())
