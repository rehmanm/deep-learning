import numpy as np

a = np.arange(9, dtype='int')

print(a)
print("array dimension: ", a.ndim)
print("array size: ",a.size)

print("T attribute: ", a.T )
print(np.transpose(a))
a.resize(3, 3)
print(a)
print("array dimension: ", a.ndim)
print("array size: ", a.size)

print("item size (of each element) depend upon the type:", a.itemsize)
print("total number of bytes array required:", a.itemsize * a.size, a.nbytes)

print("T attribute (same as Transpose): ", a.T)
print(np.transpose(a))

print("complex number represent by j in numpy")
c = np.array([1.j + 1, 5.j + 2, 3])
print(c)

print("real and imaginary part of array", np.real(c), np.imag(5))

print("dtype of array: ", a.dtype, a.dtype.str)

print("flat")
for item in a.flat:
    print(item)
print([item for item in a.flat])

