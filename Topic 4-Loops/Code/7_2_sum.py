def main():
    n = get_number()
    s = get_sum(n)
    print(s)

def get_number():
    while True:
        x = int(input("Please input a positive integer: "))
        if x>0:
            return x
            # break
    
def get_sum(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i

    return sum

main()