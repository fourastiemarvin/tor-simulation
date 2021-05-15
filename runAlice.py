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



alice = OR("Alice")
relay1 = OR("relay1")
relay2 = OR("relay2")
aliceService = OnionService("aliceService.onion")

alice.exitOR = relay1
relay1.exitOR = relay2
relay2.exitOR = aliceService

alice.start()
relay1.start()
relay2.start()
aliceService.start()

# alice encrypt n times regarding to the n nodes to the destination (extend)
time.sleep(1)
alice.sendCell(Cell("create",{"pubKey":alice.pubKey}), relay1)
# compute relay1 sharedKey
alice.sharedKey.append(alice.dh.gen_shared_key(relay1.pubKey))

time.sleep(1)
alice.sendCell(Cell("extend", {"hop":1, "pubKey":alice.pubKey, "destination":relay2.name}), relay1)
alice.sharedKey.append(alice.dh.gen_shared_key(relay2.pubKey))

time.sleep(3)
print("")
print("Keys shared: ")
print("Alice (OP):", alice.sharedKey)
print("relay 1 (first OR): ", relay1.sharedKey)
print("relay 2 (second OR): ", relay2.sharedKey)
print("")

time.sleep(3)
relay2.sockOut.connect(("", aliceService.portInOR))
