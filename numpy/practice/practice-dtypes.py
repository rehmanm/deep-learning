import numpy as np

a = np.arange(10, dtype='double')

print(a.dtype)

print(a)
print (a.shape)

b = [np.arange(10), np.arange(10, dtype='float16')]

print(b)
#print(b.shape)
#print(b.dtype)

c = np.arange(24).reshape(2,3,4)
print(c[0][0][0])
print(c.shape)
