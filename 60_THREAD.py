import concurrent.futures
import threading
import time

start=time.perf_counter()

def calculateTime(sec):
    print(f"sleep for {sec} second")
    time.sleep(sec)
    return f"Completed {sec} sleep"

with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(calculateTime,i*3) for i in range(5)]

    for r in concurrent.futures.as_completed(results):
        print(r)
        print(r.result())

finish=time.perf_counter()
print(finish-start)