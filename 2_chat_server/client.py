import socket, threading

#Constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345

ENCODER = 'utf-8'
BYTESIZE = 1024

#Client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    '''Send a message to the server to be broadcast'''
    pass


def recieve_message():
    '''Recieve an incoming message from the server'''
    while 1:
        try:
            #Recieve an incoming message from the server.
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            #Check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name:")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)

        except:
            #An error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break

#Start the client
recieve_message()
