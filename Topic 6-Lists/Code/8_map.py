# Given a list, calculate a list of square values
l = [1, 2, 3]

def square(x):
    return x ** 2

# squares = map(square, l)
squares = map(lambda x: x ** 2, l)

squares = list(squares)

print(squares)



# squares = []
# for i in l:
#     squares.append(i ** 2)

# print(squares)
