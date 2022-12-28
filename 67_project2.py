import os
import re
import threading
import time
import win32api

start=time.perf_counter()
def find_file(root_folder,rex):
    for root,dir,files in os.walk(root_folder):
        #print(root)
        for f in files:
            result=rex.search(f)
            #print(result)
            if result:
                print(os.path.join(root,f))
                break

def find_file_in_all_drives(file_name):
    rex=re.compile(file_name)
    print(rex)
    for _ in range(5):
        thread=threading.Thread(target=find_file,args=[rex])

    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        print(drive)
        #print("----",drive,rex,"+++")
        find_file(drive,rex)


find_file_in_all_drives("arha5.txt")
"""
def find_files(filename,search_path):
    result=[]
    for root,dir,files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root,filename))
    return result

print(find_files("arha5.txt","E:"))
finish=time.perf_counter()
print(finish-start)
"""