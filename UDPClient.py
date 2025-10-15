import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("Hello UDP Server!\n".encode(), ("127.0.0.1", 12345))
data, addr = client_socket.recvfrom(1024)
print("\nServer says:", data.decode())
client_socket.close()
