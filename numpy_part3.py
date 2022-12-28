import numpy as np

def numpy_function(x,y,z):
    print(x, "---------")
    print(y, "++++++++++++++++++")
    print(z, "===========")
    return 10*x+y+z

a=np.fromfunction(numpy_function,(2,3,4),dtype=int)
print(a)