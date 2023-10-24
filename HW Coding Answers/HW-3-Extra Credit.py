def print_numbers(l):
    i = 0
    s = 0
    while i<len(l):
        s += l[i]
        if s>100:
            break
        print(l[i])
        i += 1

ll = [10, 20, 50, 5, 10, 25, 30, 40]
print_numbers(ll)        