
import numpy as np

a = np.arange(1, 101)
#a.shape = (2, 5, 10)
b = a.reshape(2, 5, 10)

c = b.flatten() #Deep Copy
print(c)
c[0] = 1000
print(c)
print(b)


c = b.ravel() #Shallow Copy
print(c)
c[0] = 1000
print(c)
print(b)
print("a", end="")
print(a)
