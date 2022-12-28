n=int(input())
k=1
a=n*2-2
k=1
for i in range(n):
    for j in range(a):
        print(" ",end="")
    a-=2
    for j in range(k):
        print("*",end=" ")

    print()
