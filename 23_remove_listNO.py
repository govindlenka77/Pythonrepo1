a = set(input().split(","))
b=list(map(str,input().split(",")))
for i in b:
    if i in a:
        a.discard(i)
print(a)
