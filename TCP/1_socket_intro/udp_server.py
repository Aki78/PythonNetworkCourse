import socket

#CREATE a SERVER side socket IPV$ (AF_INET) and UPD (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind our new socket to a tuple (IP address, port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


#We are not listening or accepting connections since upd is a connectionless protocol

message, address = server_socket.recvfrom(1024)

print(message.decode("utf-8"))
print(address)
