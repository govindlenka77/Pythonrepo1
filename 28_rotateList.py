a=list(map(int,input().split()))
n=int(input())
l=n
if(n>len(a)):
    l=n-len(a)
b=a[:l]
c=a[l:]
print(c+b)