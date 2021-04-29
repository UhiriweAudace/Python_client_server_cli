import socket, sys

print("server waiting for client...\n")

server = socket.socket()
host = "10.42.0.1"
port = 65452
server.bind((host, port))
server.listen()
conn, addr = server.accept()
print(str(f"Received connection from {addr[0]} ( {addr[1]} )"))

while True:
    message = conn.recv(1024)
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