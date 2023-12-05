import numpy as np

data = np.array([23, 3, 8, 7, 56, 89, 21])

print(data.sum())
print(data.min())
print(data.max())
print(data.mean())
print(data.std())

print( np.percentile(data, 25) )
print( np.percentile(data, 50) )
print( np.percentile(data, 75) )