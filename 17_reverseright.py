n=int(input())
for i in range(n):
    for j in range(n):
        if j-i>=0:
            print(" *",end="")
        else:
            print(" ",end=" ")
    print()
