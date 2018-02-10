import numpy as np
import matplotlib.pyplot as plt

total_iteration = 10

w = 2
X = np.linspace(1, 3, total_iteration)
Y = w * X

def model(x, w):
    return np.multiply(x, w)


w_p = np.linspace(1, 3, total_iteration)
cost_array = np.ones(total_iteration).reshape(total_iteration, 1)

for i in range(total_iteration):
    y_model = model(X, w_p[i])
    cost = (1/total_iteration) *  np.sum(np.square(Y - y_model))
    cost_array[i] = cost


plt.plot(X, Y, color='r')
plt.plot(w_p, cost_array)
plt.show()











