import socket, pickle
import threading
import sys
from cell import *
import pyDH
import time
from tools import *
import ast

class OR(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.exitOR = None
        self.isConnected = False
        self.recvCell = None
        # generate DH instance
        self.dh = pyDH.DiffieHellman(5)
        self.pubKey = self.dh.gen_public_key()
        self.sharedKey = []

    # send cell to an OR
    def sendCell(self, cell, newOR, toForward=False):
        if self.isConnected == False:
            self.sockOut.connect(("", newOR.portIn))
            self.isConnected = True
        self.portOut = self.sockOut.getsockname()[1]
        if toForward:
            self.sockOut.sendall(cell)
        else:
            try:
                if cell.command == "create":
                    self.sockOut.sendall(pickle.dumps(cell))
                    print("\n %s have sent <%s> cell" % (self.name, cell.command))
                else:
                    cellToSend = cell
                    # "wrap" with all the shared keys
                    for i in range(len(self.sharedKey)):
                        j = (len(self.sharedKey) - 1) - i
                        cellToSend = pickle.dumps(encryptDecrypt(str(pickle.dumps(cellToSend)), self.sharedKey[j]))
                        # self.sockOut.sendall(pickle.dumps(encryptDecrypt(str(pickle.dumps(cell)), self.sharedKey[i])))
                    self.sockOut.sendall(cellToSend)
                    print("\n %s have sent %s" % (self.name, cell))
            except:
                cellToSend = cell
                # "wrap" with all the shared keys
                for i in range(len(self.sharedKey)):
                    j = (len(self.sharedKey) - 1) - i
                    cellToSend = pickle.dumps(encryptDecrypt(str(pickle.dumps(cellToSend)), self.sharedKey[j]))
                self.sockOut.sendall(cellToSend)
                print("\n %s have sent %s" % (self.name, cell))
    # listen to a random port (simulate dynamic IP adress)
    def run(self):
        self.sockIn.bind(("", 0))
        self.portIn = self.sockIn.getsockname()[1]
        self.sockIn.listen(1)
        print("%s is connected to the network" % (self.name))
        conn, addr = self.sockIn.accept()
        while True:
            time.sleep(1)
            data = conn.recv(4096)
            dataObj = pickle.loads(data)
            self.recvCell = str(dataObj)
            if type(dataObj) == str:
                dataObj = encryptDecrypt(dataObj, self.sharedKey[0])
            try:
                dataObj = pickle.loads(ast.literal_eval(dataObj))
            except:
                dataObj = dataObj
            if type(dataObj) == Cell:
                dataObj.execute(self)
                print("\n %s have received <%s> cell" % (self.name, dataObj.command))
            else:
                # remove an onion layer by decripting
                cellToSend = pickle.dumps(encryptDecrypt(str(pickle.dumps(dataObj)), self.sharedKey[0]))
                self.sendCell(cellToSend, self.exitOR, toForward=True)
                print("\n %s receive cell to forward" % (self.name))
            if not data:
                break
