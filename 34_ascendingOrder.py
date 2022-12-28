n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in a:
    for j in i:
        b.append(j)
b.sort()
#print(b)
l=0
c=[]
y=n
for i in range(n):
    c.append(b[l:y])

    print(b[l:y])
    #print(l,y)
    l+=n
    y+=n
print(c)
