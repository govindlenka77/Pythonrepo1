a="hsejkg 3 5 7 3 546 6 sdfg 46 546 8t5t6"
for i in a:
    if not i.isnumeric():
        a=a.replace(i," ")
l=a.split()
s=0
print(l)
for i in l:
    s+=int(i)
print(s)
print(s/len(l))
