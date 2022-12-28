import math
m=int(input())
n=int(input())
for i in range(m,n+1):
    a=math.sqrt(i)
    b=round(a)
    if(a*a==b*b):
        print(i,end=" ")
