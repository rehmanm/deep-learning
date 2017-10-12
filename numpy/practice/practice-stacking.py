import numpy as np

a = np.arange(4).reshape(2, 2)

b = a ** 2




print('hstacking')

print(np.hstack((a, b)))
print(np.concatenate((a,b), axis=1))

print('vstacking')

print(np.vstack((a, b)))
print(np.concatenate((a,b), axis=0))

print('dstacking')

print(np.dstack((a, b)))
#print(np.concatenate((a,b), axis=0))
print("column_stack == hstack")
print(np.column_stack((a, b)))

print("row_stack == vstack")
print(np.row_stack((a, b)))

print("array can be compared")
test = np.column_stack((a, b)) == np.hstack((a, b))
print(test)

