from scapy.all import *

'''

a=IP(ttl=10)
print(a)
print(a.src)
print("-"*80)


a.dst="192.168.1.1"
print(a)
print(a.src)
print("-"*80)


del(a.ttl)
print(a)
print(a.src)
print("-"*80)

b=IP()
print(b.show())
print("-"*80)
'''



c=IP() / TCP()
print(c.show())

d=Ether() / IP() / TCP()
print(d.show)

e=IP() / TCP() / "GET / HTTP /1.0\r\n\r\n"
print(e.show())

j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
print(hexdump(j))

#k=IP(dst="www.slashdot.com.org/30")
k=IP(dst="www.google.com/30")
#dst=Net('www.shashdot.org/30')
print([p for p in k])
