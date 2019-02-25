# The message should be un upper cases

import socket
from Seq import Seq

PORT = 7009
IP = "212.128.253.108"
MAX_OPEN_REQUEST = 5671


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8").split()

    seqq = Seq(msg[0])
    totalmsg = ""
    valid_seq = "ACTG"

    if msg[0] == "asdf":
        totalmsg += "ALIVE"
        cs.send(str.encode(totalmsg))
        return

    counter = 0
    for n in msg[0].upper():
        if n in valid_seq:
            counter += 1
    if counter == len(msg[0]):
        totalmsg += "OK!"
        totalmsg += "\n"
    elif counter != len(msg[0]):
        totalmsg += "Error"
        cs.send(str.encode(totalmsg))
        return

    for x in msg[1:]:
        print("Message from the client: {}".format(x))
        if x == "len":
            totalmsg += str(seqq.len())
            totalmsg += "\n"
        elif x == "complement":
            totalmsg += seqq.complement().strbases
            totalmsg += "\n"
        elif x == "reverse":
            totalmsg += seqq.reverse().strbases
            totalmsg += "\n"
        elif x == "countA":
            totalmsg += str(seqq.count("A"))
            totalmsg += "\n"
        elif x == "countC":
            totalmsg += str(seqq.count("C"))
            totalmsg += "\n"
        elif x == "countG":
            totalmsg += str(seqq.count("G"))
            totalmsg += "\n"
        elif x == "countT":
            totalmsg += str(seqq.count("T"))
            totalmsg += "\n"
        elif x == "percA":
            totalmsg += str(seqq.perc("A"))
            totalmsg += " %"
            totalmsg += "\n"
        elif x == "percC":
            totalmsg += str(seqq.perc("C"))
            totalmsg += " %"
            totalmsg += "\n"
        elif x == "percG":
            totalmsg += str(seqq.perc("G"))
            totalmsg += " %"
            totalmsg += "\n"
        elif x == "percT":
            totalmsg += str(seqq.perc("T"))
            totalmsg += " %"
        elif x != ["len", "complement", "reverse", "countA", "countC", "countG", "countT", "percA", "percC", "percG", "percT"]:
            totalmsg += "ERROR"
            cs.send(str.encode(totalmsg))
            return


# Sending the message back to the client
        # (because we are an echo server)
    cs.send(str.encode(totalmsg))


# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting or connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)

    # -- Process the client request
    clientsocket.close()
