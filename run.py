from cell import *
from OR import *
import socket
import threading

OR1 = OR("Alice")
OR2 = OR("Bob")
OR1.start()
OR2.start()
OR2.sendCell(Cell("create","message"), OR1)
OR1.sendCell(Cell("create","message"), OR2)
