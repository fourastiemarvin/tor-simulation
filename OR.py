import socket
import threading
import sys
from cell import *

class OR(threading.Thread):
    # TODO: add keys management

    def __init__(self):
        threading.Thread.__init__(self)
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.signal = True

    # send cell to an OR
    # TODO: handle different cells
    def sendCell(self, cell, newOR):
        self.sockOut.connect(("", newOR.portIn))
        self.portOut = self.sockOut.getsockname()[1]
        self.sockOut.sendall(str.encode(str(cell)))
        print("cell %s sent from port %d to port %d:" % (str(cell), self.portOut, newOR.portIn))

    # listen to a random port (simulate dynamic IP adress)
    def run(self):
        self.sockIn.bind(("", 0))
        self.portIn = self.sockIn.getsockname()[1]
        self.sockIn.listen(1)
        print("listen on port:", self.portIn)
        conn, addr = self.sockIn.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
