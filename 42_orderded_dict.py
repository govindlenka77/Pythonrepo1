from collections import OrderedDict
a=OrderedDict()
for i in range(1,5):
    a[i]=i*i
for i,j in a.items():
    print(i,j)
print(a)
print(dict(a))