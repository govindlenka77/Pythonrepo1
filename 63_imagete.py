import requests
import threading
import time
def createfile(img):
    print("file creation started")
    img_byte = requests.get(img).content
    img_name = img.split('/')[9]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_byte)
        print(f'{img_name} was downloaded...')


img_urls=[
    'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_960_720.jpg',
    'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg',
]
start=time.perf_counter()
l=[]
for img in img_urls:
    x = threading.Thread(target=createfile, args=[img])
    x.start()
    l.append(x)
    #print(x)
for i in l:
    i.join()
finish=time.perf_counter()
print(finish-start)
