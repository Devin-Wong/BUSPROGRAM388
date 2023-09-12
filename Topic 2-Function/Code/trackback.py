
def main():
    x = 20
    y = 5
    z = 3

    s = calculation(x, y, z)
    print(s)


# create function to calculate (a + b)*c
def calculation(a, b, c):
    s = add(a, b)
    r = s * c
    return r

# create a function called `add`, which can do addition.
def add(a, b):
    c = a + b
    return c

main()


















































