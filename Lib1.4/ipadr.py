from ipaddress import *
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False),

    def regular(self):
        return not (self.is_private or self.is_multicast)


netlist = []

while len(netlist) <= 50:
    netgen = IPv4RandomNetwork()
    if netgen.regular():
        netlist.append(netgen)

print(sorted(netlist))
