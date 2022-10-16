import socket


#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024


#Create a server socket, bind it to a ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Accept any incoming connection and let them know they are connected
print("Server is running...\n")
client_socket, client_address = server_socket.accept()
client_socket.send(b"You are connected to the server...\n")
