import psutil

result01=psutil.cpu_times()
result02=psutil.cpu_stats()
result03=psutil.cpu_freq()
result04=psutil.disk_partitions()
result05=psutil.net_io_counters()#pernic=True)
#pernic=False :: it collets all the sentio info from all the NICs together
print(result01)
print(result02)
print(result03)
print(result04)
print("-"*79)
print(result05)