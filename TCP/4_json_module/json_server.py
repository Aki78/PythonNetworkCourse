#Server
import socket, json

#Create a dict to represent a message packet holding all message information

message_packet = {
        "flag": "MESSAGE",
        "name": "Mike",
        "message": "this is my message.",
        "color": "#00ff3f"
        }

message_json = json.dumps(message_packet)
print(message_json)

#Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()


while 1:
    client_socket, client_address = server_socket.accept()
    print(f"connected to {client_address}\n")

    client_socket.send(message_json.encode('utf-8'))
    server_socket.close()
    break
