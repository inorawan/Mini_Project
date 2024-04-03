import socket

PORT = 8081
SERVER_ADDRESS = "127.0.0.1"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))

server_socket.listen()
print(f"Server is listening on port {PORT}")
client_socket, client_address = server_socket.accept()


file = client_socket.recv(4096).decode()
response = open('server_files/' + file).read()
client_socket.sendall(response.encode())

client_socket.close()
