def square_number(x):
    return x ** 2

def square_list(x):
    return [i**2 for i in x]

def square(*args):
    return [i ** 2 for i in args]

squares = square(2, 3)
print(squares)




# a = [2, 4, 6]

# squares = square_list(a)

# print(squares)