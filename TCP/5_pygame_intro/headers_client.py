import socket, time

#Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))


#Let's recive messages with a small bye size of 8...will not work!

time.sleep(2)
header = client_socket.recv(10)
print(header)
print(len(header))

message = client_socket.recv(int(header))

print(message.decode('utf-8'))


time.sleep(1)
header = client_socket.recv(10)
print(header)
print(len(header))

message = client_socket.recv(int(header))

print(message.decode('utf-8'))

