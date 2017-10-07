import numpy as np

a = np.arange(1, 101)

print(a[::-1]) #reverse Order
print(a[3:7])
print(a[7::-1]) #reverse from a Specific Point


b = a.reshape(2,5,10)

#print(b)

#print(b[1], end="")
print(b[1, 3, 5:3:-1])



