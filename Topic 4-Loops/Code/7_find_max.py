'''
Create a function named `get_maximum` taking a list of numbers, which can return the maximum number in the list.
'''
numbers = [10,43,25,89,90,101,13]

def get_maximum(l):
    m = l[0]
    for i in l:
        if m<i:
            m=i
    return m

print(get_maximum(numbers))