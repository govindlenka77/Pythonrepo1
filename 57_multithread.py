import threading
import time

x=time.perf_counter()
start = time.perf_counter()

def calculateTime():
    print("Sleep for 5 sec")
    time.sleep(0.99999999999)
    print("Completed sleep")
    time.sleep(1)

t1=threading.Thread(target=calculateTime)
t2=threading.Thread(target=calculateTime)
t3=threading.Thread(target=calculateTime)
t4=threading.Thread(target=calculateTime)

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
#t2.join()
t3.join()
t4.join()

finish = time.perf_counter()

print(finish-start)
t2.join()
y = time.perf_counter()
print(y-x)
