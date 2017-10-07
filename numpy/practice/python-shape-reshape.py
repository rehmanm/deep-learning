import numpy as np

a = np.arange(1, 101)

print (a)

a.reshape(2, 5, 10) #Shallow
print(a.ndim)

a.resize(2, 5, 10) #Deep
print(a.ndim)

a.shape = (100,)

print(a.ndim)

