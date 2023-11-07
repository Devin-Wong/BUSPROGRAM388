def check_prime(x):
    # for i in range(2,int(x**0.5)+1):    
    for i in range(2,x):    
        if x%i == 0:
            return False
        
    return True

l = [2, 3, 5, 40, 57, 67, 80]

prime_numbers = list(filter(check_prime, l))
print(prime_numbers)
