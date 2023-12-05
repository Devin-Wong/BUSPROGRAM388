import numpy as np

data_1 = [1, 2, 3]
data_2 = [11, 21, 31]

# --- method 2: using numpy ---------
arr1, arr2 = np.array(data_1), np.array(data_2)

print(arr1 * arr2)
# print(arr1 + arr2)
# print(arr1 - arr2)

# --- method 1: using for loop -------    
# rst = []
# for i in range(len(data_1)):
#     rst.append(data_1[i]  data_2[i])

# print(rst)