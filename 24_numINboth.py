a=list(set(map(int,input().split(","))))
b=list(set(map(int,input().split(","))))
"""
for i in a:
    if i in b:
        print(i,end=" ")
"""
a=set(a)
b=set(b)
c=a & b
print(c)
