import socket, pickle, select
import threading
import sys
from cell import *
import pyDH
import time
from tools import *
import ast

class OnionService(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sockOR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isConnected = False

    def run(self):
        self.sockOR.bind(("", 0))
        self.sockIn.bind(("", 0))
        self.sockOut.bind(("", 0))
        self.portInOR = self.sockOR.getsockname()[1]
        self.portIn = self.sockIn.getsockname()[1]
        self.sockOR.listen(1)
        conn, addr = self.sockOR.accept()
        self.sockIn.listen(1)
        print("An OR have launch the hidden server")
        print("%s is connected to the network" % (self.name))
        print("running on port:", self.sockIn.getsockname()[1])
        print("sending on port:", self.sockOut.getsockname()[1])
        portToSend = int(input("Port: "))
        self.sockOut.connect(("", portToSend))
        while True:
            if self.isConnected == False:
                conn, addr = self.sockIn.accept()
                self.isConnected = True
            message = input("> ")
            self.sockOut.sendall(pickle.dumps(message))
            data = conn.recv(4096)
            print(pickle.loads(data))
            if not data:
                break
