## find maximum value in a list
numbers = [10,43,25,89,90,101,13]

m = -9999999999
for i in numbers:
    if m<i:
        m=i

print(m)