def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    check_pythagoras(a,b,c)
    
def check_pythagoras(a, b, c):
    if a**2 + b**2 == c**2:
        print("Pythagoras theorem is satisfied.")
    else:
        print("No, Pythagoras theorem isn't satisfied.")    

main()