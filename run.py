from cell import *
from OR import *
import socket
import threading
import time

# NOTE:
#   - handle extend operations here using successive sendCell()
#   - A key exchange result in successive sends of create cell with each other

# TODO: all encryptions have to be done with pubKey of the linked OR
# TODO: code the key establishment between 3 nodes

alice = OR("Alice")
relay1 = OR("relay1")
bob = OR("Bob")
alice.exitOR = relay1
relay1.exitOR = bob

alice.start()
relay1.start()
bob.start()

time.sleep(1)
alice.sendCell(Cell("create",{"pubKey":alice.pubKey}), relay1)
# compute relay1 sharedKey
alice.sharedKey.append(alice.dh.gen_shared_key(relay1.pubKey))

# FIXME: bob gets only the alice shared key
time.sleep(1)
alice.sendCell(Cell("extend", {"hop":1, "pubKey":alice.pubKey}), relay1)
# compute bob sharedKey
relay1.sharedKey.append(relay1.dh.gen_shared_key(bob.pubKey))

time.sleep(1)
# compute bob sharedKey
alice.sharedKey.append(alice.dh.gen_shared_key(bob.pubKey))
time.sleep(1)
# print(alice.sharedKey)
# print(relay1.sharedKey)
# print(bob.sharedKey)

print("\n alice and bob shared key: ", alice.sharedKey[-1] == bob.sharedKey[0])
