from cell import *
from OR import *
import socket
import threading

OR1 = OR()
OR2 = OR()
OR1.start()
OR2.start()
OR1.join()
OR2.join()
OR1.sendCell(Cell("create","message"), OR2)