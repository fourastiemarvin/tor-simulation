import socket, pickle
import threading
import sys
from cell import *
import pyDH
import time
from tools import *
import ast

# receive unencrypted data

class OnionService(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.exitOR = None
        # self.isConnected = False
        # self.recvCell = None
        # self.portIn = port
        # self.sendTo = sendTo

# TODO: connect to Onion service and send user entry
    def run(self):
        self.sockIn.bind(("", 0))
        self.portIn = self.sockIn.getsockname()[1]
        self.sockIn.listen(1)
        print("%s is connected to the network" % (self.name))
        print("running on port:", self.sockIn.getsockname()[1])
        # conn, addr = self.sockIn.accept()
        portToSend = int(input("Port: "))
        # FIXME: sockIn or sockOut ?????
        self.sockOut.connect(("", portToSend))
        # conn, addr = self.sockOut.accept()
        # self.sockOut.connect(("", addr[1]))
        # conn, addr = self.sockIn.accept()
        while True:
            # time.sleep(1)
            # data = conn.recv(4096)
            data = self.sockIn.recv(4096)
            print(data)
            # dataObj = pickle.loads(data)
            # self.recvCell = str(dataObj)
            while True:
                message = input("> ")
                self.sockOut.sendall(message)
                break
            if not data:
                break
