from scapy.all import *

ip = IP()
print(ip)
print("-"*70)


print(ip.show())
print("-"*70)

my_frame=Ether() / IP() / TCP() / UDP() / ARP() / ICMP() #/ HTTP() HTTP is not defined in that layer
print(my_frame)
print("-"*70)
print(my_frame.show())
print("-"*70)