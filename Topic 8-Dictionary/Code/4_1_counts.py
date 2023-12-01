s = 'Rutgers, RBS'
# captalize letters
s = s.upper()

# characters in the string
chars = set(s)

# get counts and put them into a dictionary
d = dict()
for c in chars:
    count = s.count(c)
    d[c] = count
print(d)
