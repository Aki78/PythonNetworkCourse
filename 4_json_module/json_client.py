#Client
import socket, json

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

message_json = client_socket.recv(1024)
message_packet = json.loads(message_json)
print(message_packet)
print(type(message_packet))


for (key, value) in message_packet.items():
    print(f"{key}:{value}")


client_socket.close()

