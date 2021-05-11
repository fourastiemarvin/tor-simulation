from cell import *
from OR import *
from tools import *
from OnionService import *
import socket
import threading
import time
import ast

# NOTE:
# Here are the features implemented:
#   - shared keys exchanges
#   - onion routing (to send cells)
#   - start of a (pseudo-) hidden service
#
# To simplify the proof of concept, we omits the following features:
#   - circID and tables to keys handling (here each key is stored by the node)
#   - responses cells (simulated by the sender node)
#   - Rendez-vous Points and Introduction Points (simulated by communication between Onion services)
#   - Back propagation of the message received by the server (work like onion routing)
#
# we can also note that the Onion Proxy (OP) is implemented as a Onion Router (OR)
# that compute shared keys for every nodes in the circuit.
# See the documents to more detailed explanation about the design


bob = OR("bob")
relay1 = OR("relay1")
relay2 = OR("relay2")
bobService = OnionService("bobService.onion")
bob = OR("Bob")

bob.exitOR = relay1
relay1.exitOR = relay2
relay2.exitOR = bobService

bob.start()
relay1.start()
relay2.start()
bobService.start()

# bob encrypt n times regarding to the n nodes to the destination (extend)
time.sleep(1)
bob.sendCell(Cell("create",{"pubKey":bob.pubKey}), relay1)
# compute relay1 sharedKey
bob.sharedKey.append(bob.dh.gen_shared_key(relay1.pubKey))

time.sleep(1)
bob.sendCell(Cell("extend", {"hop":1, "pubKey":bob.pubKey, "destination":relay2.name}), relay1)
relay1.sharedKey.append(relay1.dh.gen_shared_key(relay2.pubKey))
bob.sharedKey.append(bob.dh.gen_shared_key(relay2.pubKey))

time.sleep(3)
print("")
print("Keys shared: ")
print("bob (OP):", bob.sharedKey)
print("relay 1 (first OR): ", relay1.sharedKey)
print("relay 2 (second OR): ", relay2.sharedKey)
print("")

time.sleep(3)
relay2.sockOut.connect(("", bobService.portInOR))
