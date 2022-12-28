s=1
i=0
l=[]
x=set()
y=[]
while(s<100):
    #print(s, end=" ")
    i+=1
    if(i%6==0):
        i+=1
    s+=(i*3)
    l.append([z for z in str(s)])
    y.append(set(str(s)))
    #print(set(str(s)))
    x.update(set(str(s)))
#print()
print(l)
print(x)
print(y)
i=0
count=0
while(i<len(l)):
    if l[0]==list(y[0]):
        count+=1
print(count)