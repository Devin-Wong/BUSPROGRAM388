''' to calculate the area of a circle. The formula is pi*r^2 (let pi=3.14), where r denotes radius. 

(1) create a function named `square`, which returns the square if inputing a value. 
(2) create a function named `area`, which returns the circle area if input radius. In this function, you call `square` function.
(3) print sentence like "The area of a circle with redius 1 is 3.14.".
(4) use `main()` function to orgnize your program.
'''

def main():
    radius = float(input("Please input radius: "))
    a = area(radius)
    print(f"The area of a circle with redius {radius} is {a}.")

    
def square(a):
    s = a**2
    return s

def area(r):
    s = 3.14 * square(r)   
    return s

main()