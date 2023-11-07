
l = ['Rbs', 'Rutgers', 'bait', 'mis'] 

## method 2:
# l_upper = [x.upper() for x in l]
# print(l_upper)

# ## method 1:
def captalize(x):
    return x.upper()

# l_upper = list(map(captalize, l))

l_upper = list(map(lambda x: x.upper(), l))

print(l_upper)