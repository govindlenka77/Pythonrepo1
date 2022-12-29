import socket
print()
x=socket.gethostname()
print("Hostname: ",x)
ipadd=socket.gethostbyname(x)
print(ipadd,type(ipadd))