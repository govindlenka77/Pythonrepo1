import time

start = time.perf_counter()
print(start)

#global c
def calculateTime():
    print("Sleep for 5 sec")
    time.sleep(0.99999999999)
    print("Completed sleep")
    time.sleep(1)

calculateTime()
calculateTime()
calculateTime()
finish = time.perf_counter()
print(finish-start)
print(start)
