from cell import *
from OR import *
from tools import *
import socket
import threading
import time
import ast

# NOTE:
#   - handle extend operations here using successive sendCell()
#   - A key exchange result in successive sends of create cell with each other

# TODO: all encryptions have to be done with pubKey of the linked OR
# TODO: encrypt every exchanges

alice = OR("Alice")
relay1 = OR("relay1")
bob = OR("Bob")
alice.exitOR = relay1
relay1.exitOR = bob
#
alice.start()
relay1.start()
bob.start()

time.sleep(1)
alice.sendCell(Cell("create",{"pubKey":alice.pubKey}), relay1)
# compute relay1 sharedKey
alice.sharedKey.append(alice.dh.gen_shared_key(relay1.pubKey))
#
time.sleep(1)
# alice.sendCell(Cell("extend", {"hop":1, "pubKey":None}), relay1)
# # compute bob sharedKey
# relay1.sharedKey.append(relay1.dh.gen_shared_key(bob.pubKey))
#
# # time.sleep(1)
# # compute bob sharedKey
# # alice.sharedKey.append(alice.dh.gen_shared_key(bob.pubKey))
# time.sleep(3)
# print(alice.sharedKey)
# print(relay1.sharedKey)
# print(bob.sharedKey)
# print(relay1.sharedKey[-1] == bob.sharedKey[-1])

print("------TESTS-------")
# alice.sendCell(encryptDecrypt(str(Cell("create",{"pubKey":alice.pubKey})), alice.sharedKey[0]), relay1)
print(pickle.dumps(Cell("create",{"pubKey":None})))
a = encryptDecrypt(str(pickle.dumps(Cell("create",{"pubKey":None}))), alice.sharedKey[0])
print(a + "\n")
b = encryptDecrypt(a, alice.sharedKey[0])
print(b)
print(type(b))
print(type(ast.literal_eval(b)))
print(pickle.loads(ast.literal_eval(b)))
print(pickle.loads(ast.literal_eval(b)).command)

# print(encryptDecrypt(a, alice.sharedKey[0]))

# time.sleep(2)
# print(encryptDecrypt(relay1.recvCell,relay1.sharedKey[-1]))


# a = encryptDecrypt(relay1.recvCell, relay1.sharedKey[-1])
# b = encryptDecrypt(a, bob.sharedKey[0])
# print(a)
# print(b)
# print(a == b)
