import socket
import threading
import sys
from cell import *

class OR(threading.Thread):
    # TODO: add keys management

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)
        self.socket = sock
        self.signal = True

    # send cell to an OR
    # TODO: handle different cells
    def sendCell(self, cell, newOR):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", newOR.portIn))
        sock.sendall(str.encode(str(cell)))
        print("cell sent:", str(cell))

    # wait for connection
    def newConnections(self):
        while True:
            sock, address = self.socket.accept()
            print(address,"connected")

    # listen to a random port (simulate dynamic IP adress)
    def run(self):
        self.socket.bind(("", 0))
        self.portIn = self.socket.getsockname()[1]
        print("running on port:", self.portIn)
        self.socket.listen(1)

        #Create new thread to wait for connections
        newConnectionsThread = threading.Thread(target = self.newConnections)
        newConnectionsThread.start()
