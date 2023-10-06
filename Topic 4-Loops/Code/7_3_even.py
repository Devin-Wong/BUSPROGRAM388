
l = ["a", "b", "c", "d", "e", "f"]

def print_even_elements(l):
    for i in range(len(l)):
        if i%2==0:
            continue
        print(l[i])

print_even_elements(l)