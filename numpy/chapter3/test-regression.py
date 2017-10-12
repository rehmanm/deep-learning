import numpy as np
import matplotlib.pyplot as plt

N = 2

data = np.loadtxt("data.csv", delimiter=",", usecols=(0,1), unpack=True)

print(data)

calls = data[0]
aht = data[1]

A = np.vstack([calls, np.ones(len(calls))]).T

lst = np.linalg.lstsq(A, aht)
m, c = lst[0]
residual = lst[1]
r2 = 1 - residual / sum((aht - aht.mean())**2)

print("Slope = ", m)
print("Constant = ", c)
print("Residual = ", residual)
print("R2 = ", r2)



plt.plot(calls, aht, 'o', label='Original data', markersize=3)
plt.plot(calls, m*aht + c, 'r', label='Fitted line')
plt.legend()
plt.show()