import socket
import termcolor

# Change this IP to yours!!!!!
IP = "212.128.253.79"
PORT = 8089
MAX_OPEN_REQUESTS = 57


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    if msg != '':
        print()
        print("Request message: ")
        termcolor.cprint(msg, 'green')

        request = msg.partition('\n')[0].split(' ')[1]

        content = ''
        if request == '/':
            with open('index.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        elif request == '/blue':
            with open('blue.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        elif request == '/pink':
            with open('pink.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)
        else:
            with open('error.html', 'r') as file:
                for line in file:
                    content += line
                    content = str(content)

        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {}\r\n".format(len(str.encode(content)))

        response_msg = status_line + header + "\r\n" + content

        cs.send(str.encode(response_msg))

    else:
        print("Your request is empty ):")
    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
