n = int(input())
y = n%365
w = y%7
a = "years:{0}  weeks: {1}  days: {2}".format(n//365, y//7, w)
print(a)
