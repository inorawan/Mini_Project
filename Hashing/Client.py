import socket
import webbrowser

PORT = 8080
SERVER_ADDRESS = "127.0.0.1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, PORT))

file = input("Enter the file name: ")
url = f"GET/ {file} HTTP/1.1\r\nHost:localhost\r\n\r\n"
client_socket.send(url.encode())
response = client_socket.recv(4096).decode()
webbrowser.open('file3.html')
print(response)

client_socket.close()
