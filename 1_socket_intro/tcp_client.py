import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port

client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
