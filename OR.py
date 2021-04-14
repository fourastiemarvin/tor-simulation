import socket, pickle
import threading
import sys
from cell import *

class OR(threading.Thread):
    # TODO: add keys management

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.signal = True

    # send cell to an OR
    def sendCell(self, cell, newOR):
        self.sockOut.connect(("", newOR.portIn))
        self.portOut = self.sockOut.getsockname()[1]
        self.sockOut.sendall(pickle.dumps(cell))
        print("cell %s sent from port %d to port %d:" % (str(cell), self.portOut, newOR.portIn))

    # TODO: handle different cells
    # listen to a random port (simulate dynamic IP adress)
    def run(self):
        self.sockIn.bind(("", 0))
        self.portIn = self.sockIn.getsockname()[1]
        self.sockIn.listen(1)
        print("%s listen on port:%s" % (self.name,self.portIn))
        conn, addr = self.sockIn.accept()
        with conn:
            print("%s connected to %s" % (addr, self.name))
            while True:
                data = conn.recv(1024)
                dataObj = pickle.loads(data)
                print("%s received by %s" % (dataObj.command,self.name))
                dataObj.execute(self)
                if not data:
                    break
