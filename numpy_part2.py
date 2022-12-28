import numpy as np

array_x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(array_x)
print(array_x.size)
print(array_x[1,2])
print(array_x[0,2])
print(array_x[:, 2])
print(array_x[: , -3])

# step - start :end: stepsize
print(array_x[0, 0: 5: 2])

print(array_x[:, 0: 4: 2])

array_x[0,2] = 10
array_x[:,2] = 10
print(array_x)
