def main():
    x = get_number()
    get_factors(x)

def get_number():
    while True:
        x = int(input("Please input a positive number: "))
        if x>0:
            break
    return x

def get_factors(x):
    for i in range(1, x+1):
        if x%i==0:
            print(i)

main()            