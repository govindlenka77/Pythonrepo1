n=int(input())
a=2*n-2
k=1
for i in range(n):
    for j in range(a//2):
        print(" ",end=" ")
    a-=2
    for j in range(k):
        if(j==0 or j==k-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    k+=2
    print()
l=0
k-=2
for i in range(n):
    l += 1
    k -= 2
    for j in range(l):
        print(" ",end=" ")
    for j in range(k):
        if(j==0 or j==k-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
