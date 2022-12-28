import threading
import time
r=time.perf_counter()
def calculatetime(a):   #ERROR
    i=0
    print("srart")
    time.sleep(a)
    i+=1
    print("End")

a=[]
for i in range(5):
    x=threading.Thread(target=calculatetime,args=[1])
    x.start()
    a.append(x)
for i in a:
    i.join()
s=time.perf_counter()
print(s-r)
print(type(a[0]))