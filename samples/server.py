import socket
import threading
from client import Client

#Variables for holding information about connections
connections = []
total_connections = 0

#Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1

def main():
    #Get host and port
    # host = input("Host: ")
    # port = int(input("Port: "))
    # port = 1818
    port = 0

    #Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    # sock.bind(("1",port))
    print("running on port:", sock.getsockname()[1])
    sock.listen(5)

    #Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()

main()
