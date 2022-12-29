from scapy.all import *

s=IP(dst="google.com")/ICMP()           #learn CIDR
print(s.show())