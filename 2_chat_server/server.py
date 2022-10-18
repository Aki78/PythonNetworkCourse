import socket, threading

#Constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024


#Server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []

def broadcast_message(message):
    '''Send a message to all clients connected to the server'''
    for client_socket in client_socket_list:
        client_socket.send(message)

def recieve_message(client_socket):
    '''Recieve an incoming message from a specific client and forward the message to be broadcast'''
    while 1:
        try:
            #Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)

        except:
            #Find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            #Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            #Broadcast that the client has left the chat.
            client_socket.close()
            break

def connect_client():
    '''connect an incoming client to the server'''
    while 1:
        #Accept incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        #Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        #Add new client socket and client name to appropriate list
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #Update the server, individual client, and all clients
        print(f"Name of new client is {client_name}\n") #server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER)) #Individual client
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER))
        recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
        recieve_thread.start()

#Start server
print("Server is listening for incoming connections...\n")
connect_client()
