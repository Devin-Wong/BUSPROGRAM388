# filter, positive values
l = [1, -2, 3, -4]

## ----- filter & lambda -------------
positive_numbers = list(filter(lambda x: x>0, l))
print(positive_numbers)

## ----- use filter --------------
# def is_positive(x):
#     return x>0

# positive_numbers = list(filter(is_positive, l))

# ## ----- use for loop ------
# positive_numbers = []
# for i in range(len(l)):
#     if l[i]>0:
#         positive_numbers.append(l[i])
# print(positive_numbers)        