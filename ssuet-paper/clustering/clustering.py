
import numpy as np
import matplotlib.pyplot as plt


c1 = np.random.random_sample(size = (2, 10)) +.5

c2 = np.random.random_sample(size = (2, 10)) + 3.5


c3 = np.stack([c1, c2], axis=1)

'''

print(c3)

xs = np.arange(10)

plt.plot(xs, c3[0][0], 'g-', label='Array1')
plt.plot(xs, c3[0][1], 'r-', label='Array2')


plt.plot(xs, c3[1][0], 'g-.', label='Array3')
plt.plot(xs, c3[1][1], 'r-.', label='Array4')

std=np.std(c3)
m = np.mean(c3)
print(m, std)


plt.errorbar(m,0,xerr=std,fmt='|', ms=30,mew=2,capthick=2,capsize=10)

plt.show()
'''


labels = list('ABCDEFGHIJ')
data = np.concatenate((c3[0], c3[1], c3[1], c3[0]), 0)
plt.boxplot(data, showmeans=True, labels=labels )
plt.show()


