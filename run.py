from cell import *
from OR import *
import socket
import threading
import time

# NOTE: handle extend operations here using successive sendCell()

OR1 = OR("Alice")
OR2 = OR("Bob")
OR1.start()
OR2.start()
OR2.sendCell(Cell("create",{"hop":0 ,"pubKey":OR2.pubKey}), OR1)
OR1.sendCell(Cell("create",{"hop":0, "pubKey":OR1.pubKey}), OR2)
time.sleep(1)
print(OR1.sharedKey == OR2.sharedKey)
