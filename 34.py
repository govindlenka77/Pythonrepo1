n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    if(i==n-1):
        b+=a
print(b)
b.sort()
#print(b)
l=0
c=[]
y=n
for i in range(n):
    c.append(b[l:y])
    #print(b[l:y])
    #print(l,y)
    l+=n
    y+=n
print(c)
