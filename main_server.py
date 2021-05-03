""" import required package"""
import socket

HOST = "172.20.10.2"
PORT = 65452


def run_server(packet_size=1024):
    """ This method will run our chat server and will receive packet
        based on the specified packet size, by default will receive 1024 bytes
    """
    server = socket.socket()
    addr = (HOST, PORT)
    server.bind(addr)
    server.listen()
    print("Awaiting for client to connect...")

    conn, addr = server.accept()
    client_ip = addr[0]
    client_port = addr[1]
    print(str(f"Received connection from {client_ip}:{client_port}"))

    while True:
        message = conn.recv(packet_size)
        message = message.decode()
        rcvd_message = message.strip().split('|')
        print("Client: ", message)
        input_message = input(str("Me: "))
        msg_id = rcvd_message[1]
        msg_type = 'Response'
        message = f'Py|{msg_id}|{msg_type}|{input_message}'
        if input_message == "quit":
            message = "Left chat room!"
            conn.send(message.encode())
            print("\n")
            break
        conn.send(message.encode())
    conn.close()
    server.close()
