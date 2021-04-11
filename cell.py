class Cell():
    def __init__(self, command, payload):
        self.command = command
        self.payload = payload

    def __str__(self):
        return ("<" + str(self.command) + " : "
                   + str(self.payload) + ">")

    def execute(self, orSend, orRecv):
        # creat a connection with a new node
        if self.command == "create":
            # receiver will listen at a new port
            orRecv.bind(("", 0))
            # receiver set the port to connect of the sender
            orSend.portOut = orRecv.portIn

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
