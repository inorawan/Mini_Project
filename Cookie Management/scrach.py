
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8081

def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    headers = request_data.split('\n')

    if 'GET /set-cookie' in headers[0]:
        # Set a cookie
        response = "HTTP/1.1 200 OK\nSet-Cookie: popup_accepted=true; Path=/\nContent-Length: 0\n\n"
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()
        return

    # HTTP response
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n"

    response += "\n"  # End of headers

    # HTML content with popup and buttons
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accept or Reject Popup</title>
    <style>
    /* Style for the popup */
    .popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 40px; /* Increased padding */
        border: 2px solid #ccc; /* Increased border size */
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2); /* Increased shadow */
        z-index: 1000;
        width: 400px; /* Increased width */
        max-width: 80%; /* Set maximum width */
    }

    /* Style for the popup title */
    .popup h2 {
        font-size: 24px; /* Increased font size */
        margin-bottom: 20px; /* Increased margin */
    }

    /* Style for the popup message */
    .popup p {
        font-size: 18px; /* Increased font size */
        margin-bottom: 20px; /* Increased margin */
    }

    /* Style for the buttons */
    .btn {
        padding: 15px 30px; /* Increased padding */
        margin: 0 20px; /* Increased margin */
        cursor: pointer;
        font-size: 18px; /* Increased font size */
    }

    /* Style for the accept button */
    .accept {
        background-color: green;
        color: white;
    }

    /* Style for the reject button */
    .reject {
        background-color: red;
        color: white;
    }
</style>

</head>
<body>
    <h2>Cookie Management</h2>
    <div class="popup">
        <h2>Popup Message</h2>
        <p>This is a popup message. Please accept or reject.</p>
        <button id="btn accept" onclick="acceptClicked()">Accept</button>
        <button id="onetrust-reject-all-handler" onclick="rejectClicked()">Reject</button>
    </div>

    <script>
        function acceptClicked() {
            // Close the popup
            document.querySelector('.popup').style.display = 'none';
            // Send a request to set the cookie
            fetch('/set-cookie', {
                method: 'GET'
            });
        }

        function rejectClicked() {
            // Close the popup
            document.querySelector('.popup').style.display = 'none';
        }
    </script>
</body>
</html>

    """

    response += html_content

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f'Server listening on {HOST}:{PORT}')

        while True:
            client_socket, client_address = server_socket.accept()
            print(f'Connected by {client_address}')
            handle_client(client_socket)

if __name__ == "__main__":
    run_server()
