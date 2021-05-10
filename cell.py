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
            OR.sharedKey.append(OR.dh.gen_shared_key(self.payload["pubKey"]))
        # extend the network by 1
        elif self.command == "extend":
            if self.payload["hop"] == 1:
                self.command = "create"
                OR.sendCell(self,OR.exitOR)
