
import socket
import hashlib
import shutil
from cryptography.fernet import Fernet

PORT_CLIENT = 8080
PORT_SERVER = 8081
SERVER_ADDRESS = "127.0.0.1"
CODE = 1234

serverA_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverA_socket.bind(("0.0.0.0", PORT_CLIENT))

key = Fernet.generate_key()
fernet = Fernet(key)
database = { }

def verify_integrity(content, filename):
    calc_hash = hashlib.sha256(content.encode()).hexdigest()
    actual_hash = fernet.decrypt(database[filename]).decode()

    return calc_hash == actual_hash

def handle_request(request):
    headers = request.split('\n')
    filename = headers[0].split()[1]

    try:
        fin = open(filename)
        content = fin.read()
        fin.close()

        if verify_integrity(content, filename):
            print("Successful verification of Hash")
            response = 'HTTP/1.0 200 OK\n\n' + content
        else:
            print("Invalid hash verification: Redireciting to server 1")
            serverB_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverB_socket.connect((SERVER_ADDRESS, PORT_SERVER))
            serverB_socket.send(filename.encode())
            response = serverB_socket.recv(4096).decode()
            print("Successful hash verification at server 1\n Data received from server 1: \n")
            print(response)
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return response

def print_db():
    for key in database:
        print(f"{key} : {database[key]}\n")

serverA_socket.listen()
print(f"Server is listening on port {PORT_CLIENT}")
client_socket, client_address = serverA_socket.accept()

print("Server operates in 3 states: \n\t1. Accepts request from client\n\t2. Updation of content\n\t3. Terminate connection\n")

while True:
    state = int(input("Enter a state: "))

    match state:
        case 1:
            request = client_socket.recv(4096).decode()
            response = handle_request(request)

            client_socket.sendall(response.encode())
        case 2:
            code = int(input("Enter authentication code: "))
            if code==CODE:
                filename = input("Enter the file to be uploaded: ")
                file = open(filename)
                file = file.read()
                shutil.copy(filename, 'server_files/')

                hash = hashlib.sha256(file.encode()).hexdigest()
                hash_encoded = fernet.encrypt(hash.encode())
                database[filename] = hash_encoded
                print_db()
            else:
                print("INVALID AUTHENTICATION CODE")
        case 3:
            client_socket.close()
            break;


