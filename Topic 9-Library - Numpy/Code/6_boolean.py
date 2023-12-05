import numpy as np
data = np.array([23, 3, 8, 7, 56, 89, 21])

# print(data > 10)

print( data[data>10] )

print(data[data%2 == 0])

print(data[data%2 != 0])