import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))
client_socket.send("Hello Server!\n".encode())
data = client_socket.recv(1024).decode()
print("\nServer says:", data)
client_socket.close()