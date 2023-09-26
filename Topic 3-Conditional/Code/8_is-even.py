'''
Create a function named `is_even`, which returns `True` if inputting a even number; return `False`.
'''

def main():
    n = int(input("Please input an integers: "))

    if is_even(n):
        print("It is a even number!")
    else:
        print("It is an odd number!")    

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()