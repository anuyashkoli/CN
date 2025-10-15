import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))
print("\nUDP Server is ready and waiting for message...")
data, addr = server_socket.recvfrom(1024)
print("\nClient says:", data.decode())
server_socket.sendto("Hello Client, received your UDP message!\n".encode(), addr)
server_socket.close()