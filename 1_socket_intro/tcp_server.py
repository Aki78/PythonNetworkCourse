import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname()) #hostname
print(socket.gethostbyname(socket.gethostname())) # ip of the given hostname

# Bind our new socket to a tuble (IP Address, port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


# put the socket into listening mode to listen for any possible connections

#Listen forever to accept ANY connection
server_socket.listen()

while 1:
    #Accept every single connection and store two piecese of information
    client_socket, client_address = server_socket.accept()
    print("Hej")
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)
    print(f"Connect to {client_address}!\n")
