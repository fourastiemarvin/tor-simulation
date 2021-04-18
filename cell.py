import pyDH

class Cell():
    def __init__(self, command, payload):
        self.command = command
        self.payload = payload

    def __str__(self):
        return ("< " + str(self.command) + " : "
                   + str(self.payload) + " >")

    def execute(self,OR):
        # create a connection with a new node
        if self.command == "create":
            # check if the receiver is the good one
            if self.payload["hop"] == 0:
                # create sharedKey using received pubKey
                OR.sharedKey = OR.dh.gen_shared_key(self.payload["pubKey"])
                print(OR.sharedKey)
            else:
                self.payload["hop"] -= 1
        elif self.command == "extend":
            return None
        elif self.command == "destroy":
            return None
        else:
            print("Unknown command")

# class ControlCell():
#     def __init__(self, command, payload):
#         self.command = command
#         self.payload = payload
#
#     def __str__(self):
#         return str(self.command) + " : " + str(self.payload)
#
#     def execute(self):
#         if self.command == "create":
#             return None
#         elif self.command == "destroy":
#             return None
#         else:
#             print("Unknown command")
#
# class RelayCell():
#     def __init__(self, command, payload):
#         self.command = command
#         self.payload = payload
#
#     def execute(self):
#         if self.command == "data":
#             return None
#         elif self.command == "begin":
#             return None
#         elif self.command == "end":
#             return None
#         elif self.command == "connected":
#             return None
#         elif self.command == "extend":
#             return None
#         else:
#             print("Unknown command")
