a=list(map(str,input().split(",")))
l=[]
for i in a:
    if i.isnumeric():
        l.append(i)
print(l)

