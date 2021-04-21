import socket, pickle
import threading
import sys
from cell import *
import pyDH
import time

class OR(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.exitOR = None
        self.isConnected = False
        # generate private key
        self.dh = pyDH.DiffieHellman(5)
        self.pubKey = self.dh.gen_public_key()
        self.sharedKey = []

    # send cell to an OR
    def sendCell(self, cell, newOR):
        if self.isConnected == False:
            self.sockOut.connect(("", newOR.portIn))
            self.isConnected = True
        self.portOut = self.sockOut.getsockname()[1]
        self.sockOut.sendall(pickle.dumps(cell))
        print("\n %s have sent <%s> cell" % (self.name, cell.command))

    # listen to a random port (simulate dynamic IP adress)
    def run(self):
        self.sockIn.bind(("", 0))
        self.portIn = self.sockIn.getsockname()[1]
        self.sockIn.listen(1)
        print("%s is connected to the network" % (self.name))
        conn, addr = self.sockIn.accept()
        while True:
            time.sleep(1)
            data = conn.recv(1024)
            dataObj = pickle.loads(data)
            print("\n %s have received <%s> cell" % (self.name, dataObj.command))
            dataObj.execute(self)
            if not data:
                break
