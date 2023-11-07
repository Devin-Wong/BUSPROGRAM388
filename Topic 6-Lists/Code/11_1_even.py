l = [2, 3, 10, 17, 20]

## ----- method 2: use comprehension ---------
even_numbers = [i for i in l if i%2==0]
print(even_numbers)

## ----- method 1: use for loop and append method --------
# even_numbers = []
# for i in l:
#     if i%2 == 0:
#         even_numbers.append(i)

# print(even_numbers)