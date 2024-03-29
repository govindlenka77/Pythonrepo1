import requests
import time

img_urls=[
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
]
t1=time.perf_counter()

for img in img_urls:
    img_byte=requests.get(img).content
    img_name = img.split('/')[3]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as img_file:
        img_file.write(img_byte)
        print(f'{img_name} was downloaded...')
finish=time.perf_counter()
print(f'Finished in {finish-t1}')