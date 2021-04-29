import socket, sys

print("server waiting for client...\n")

s = socket.socket()
# host = socket.gethostname()
host = "10.42.0.1"
port = 65452
s.bind((host, port))
print(host,"\n")
# name = input(str("Enter your name: "))
           
s.listen()
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

while True:
    message = conn.recv(1024)
    message = message.decode()
    rcvd_message = message.strip().split('|')
    print("Client: ", message)
    input_message = input(str("Me: "))
    msg_id = rcvd_message[1]
    msg_type = 'Response'
    message = f'Py|{msg_id}|{msg_type}|{input_message}'
    if message == "quit":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())