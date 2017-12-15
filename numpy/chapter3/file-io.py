import numpy as np

a = np.eye(2)
print(a)
b = np.ones(9, dtype='int').reshape(3, 3)
print(b)

c = np.zeros(9).reshape(3, 3)
print(c)

np.savetxt("zeros.txt", b)

(revenue, fabunits) = np.loadtxt("data.csv", delimiter=",", usecols=(0, 1), unpack=True)

print("Weighted Average =", np.average(revenue, weights=fabunits))
print("Mean =", np.mean(revenue))

l = np.arange(len(revenue))
print("Time Weighted Average = ", np.average(revenue, weights=l))

print("max = ", np.max(revenue))
print("min = ", np.min(revenue))
print("peak to peak distance (Difference between Max and Min) = ", np.ptp(revenue))
#print("mode = ", np.mode(revenue))
print(revenue, np.sort(revenue))
print("median = ", np.median(np.msort(revenue)))
print(revenue.mean())
print("variance = ", np.var(revenue), np.meanx                                ((revenue - revenue.mean())**2))





