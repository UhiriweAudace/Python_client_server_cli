""" import required package"""
import socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 65452
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def run_server(packet_size):
    """ This method will run our chat server and will receive packet
        based on the specified packet size, by default will receive 1024 bytes
    """
    SOCK.bind((HOST, PORT))
    print(f"[host] - {HOST}")

    SOCK.listen()
    conn, addr = SOCK.accept()
    print(f"[connection] - {addr[0]}:{addr[1]}\n")
    buffer_size_msg = f'My buffer size: {packet_size}'
    conn.send(buffer_size_msg.encode())
    client_message = ''
    msg_count = 1
    while True:
        final_packet_size = packet_size+2
        client_received_msg = conn.recv(final_packet_size)
        splitted_msg = client_received_msg.decode().split('|')
        client_message += splitted_msg[0]
        try:
            if msg_count == int(splitted_msg[1]):
                continue
        except IndexError:
            print("[Client]: ", client_message)

        client_message = ''
        input_message = input(str("[Server]: "))
        message = str(input_message)
        message_parts = [message[i:i+packet_size]
                         for i in range(0, len(message), packet_size)]
        for index, value in enumerate(message_parts):
            final_message_parts = ''
            if message_parts[index] != message_parts[len(message_parts) - 1]:
                final_message_parts = str(f'{value}|{msg_count}')
            else:
                final_message_parts = str(f'{value}')
            conn.send(final_message_parts.encode())

        msg_count += 1
