a=list(map(int,input().split()))
k=int(input())
l=list()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]+a[j]==k):
            r=[a[i],a[j]]
            l.append(r)
print(l)
