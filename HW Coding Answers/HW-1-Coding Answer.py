def main():
    radius = 3
    height = 4
    s = surface(radius, height)
    print(f"The surface of a cylinder with base radius {radius} and height {height} is {s}")

def add(a, b):
    c = a + b
    return c

def surface(radius, height):
    s = 2 * 3.14 * radius * add(radius, height)
    return s

main()