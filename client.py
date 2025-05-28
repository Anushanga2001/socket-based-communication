import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Connect to server

client_socket.send("Hello Server!".encode())
response = client_socket.recv(1024).decode()
print("Server says:", response)

client_socket.close()