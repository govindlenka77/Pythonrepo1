n=input()
l=set(n)
for i in l:
    if(i!=" "):
        p=n.count(i)
        print(i,":",p)
