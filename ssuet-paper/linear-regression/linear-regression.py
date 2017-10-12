#from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

N = 2

data = np.loadtxt("data.csv", delimiter=",", usecols=(0,1), unpack=True)

print(data)

size = data[0]
price = data[1]

A = np.vstack([size, np.ones(len(size))]).T

lst  = np.linalg.lstsq(A, price)
m, c = lst[0]
residual = lst[1]
r2 = 1 - residual / sum((price - price.mean())**2)

print("Slope = ", m)
print("Constant = ", c)
print("Residual = ", residual)
print("R2 = ", r2)



plt.plot(size, price, 'o', label='Original data', markersize=10)
plt.plot(size, m*size + c, 'r', label='Fitted line')
plt.legend()
plt.show()