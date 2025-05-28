import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # IP + Port
server_socket.listen()

print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected with {addr}")

# Receive and send message
message = conn.recv(1024).decode()
print("Client says:", message)
conn.send("Hello from server!".encode())

conn.close()