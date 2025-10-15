import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)
print("\nServer is waiting for connection...")
conn, addr = server_socket.accept()
print("\nConnected by", addr)
data = conn.recv(1024).decode()
print("\nClient says:", data)
conn.send("Hello Client, message received!\n".encode())
conn.close()
server_socket.close()