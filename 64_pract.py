import os
f='E:\\prac1\\demo.py'

path=os.path.realpath(__file__)
dir=os.path.dirname(path)
dir.replace('p1','p2')
os.chdir(dir)
print(path,dir)
print(path)