#keyword arguments
#positional arguments
#arguments(args)
#default arguments
def ret(*args):
    return args[0]

def prefil(a):
    return "Welcome "+a

def sqr(c):
    a=list(map(int,c.split(",")))
    b=[]
    for i in a:
        b.append(i*i)
    return b

def div7(a):
    if(a%7==0):
        return True
    else:
        return False

def areape(**kargs):
    area=kargs["length"]*kargs["length"]
    peri=kargs["length"]*4
    return area,peri

def nam(a):
    return a[1]

def lowup(a):
    b=0
    c=0
    for i in a:
        if i.isupper():
            b+=1
        elif i.islower():
            c+=1
    return b,c

def win(a):
    l=list(map(int,a.split()))
    w=l[0]*4
    d=l[1]*2
    lo=l[2]
    return w+d-lo

def marcopolo(a):
    if(a%3==0 and a%5==0):
        return "MarcoPolo"
    elif(a%3==0):
        return "Marco"
    elif a%5==0:
        return "Polo"
    else:
        return a

def bill(a):
    if(a<500):
        return a-(0.05*a),0.05*a
    elif a>=500 and a<2500:
        return a-(0.1*a),0.1*a
    elif a>=2500:
        return a-(0.2*a),0.2*a

def summin(a):
    for i in a:
        if not i.isdigit():
            a=a.replace(i," ")
    l=list(map(int,a.split()))
    return sum(l),min(l),max(l)

def fact(a):
    b=1
    if(a<0):
        return "Invalid"
    elif a==0:
        return 1
    else:
        b=a*fact(a-1)
    return b

def sum1(a):
    s=0
    if(a==0):
        return 0
    else:
        s=a+sum1(a-1)
    return s


def remlist(a,b):
    c=[]
    for i in a:
        if i!=b:
            c.append(i)
    return c


a=ret(7)
print(a)
#
name="HCL"
b=prefil(name)
print(b)
#
c="1,2,3,4"
d=sqr(c)
#
print(d)
#
print(div7(21))
#
e,f=areape(length=20)
print(e,",",f)
#
g="name"
print(nam(g))
#
h="PYthOn"
i,j=lowup(h)
print(i,",",j)
#
k="5 3 5"
l=win(k)
print(l)
#
m=marcopolo(30)
print(m)
#
n1,n2=bill(100)
print(n1,n2)
#
p="12d45cd45 4 5gf5g5"
q,r,s=summin(p)
print(q,r,s)
#
print(fact(5))
#
print(sum1(10))
#
t=[1,2,3,1,5,7,1,2,7,1,3]
u=1
print(remlist(t,u))
#
