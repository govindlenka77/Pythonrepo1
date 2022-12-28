h="Pass@w1345"
a=False
b=False
c=False
d=False
e=False
for i in h:
    if(i.isupper()):
        a=True
    if(i.isdigit()):
        b=True
    if(i=='@'):
        c=True
    if(i.islower()):
        d=True
p=len(h)
if(p>7):
    e=True
if(a and b and c and d and e):
    print("Valid")
else:
    print("Invalid")