import socket

# SERVER IP, PORT

PORT = 5678
IP = "191.168.0.139"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    msg = input("> ")

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print(response)

    s.close()
