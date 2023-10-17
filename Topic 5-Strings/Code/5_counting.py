# count the number of times a letter appears in a string
## For example, 'RBS, Rutgers',
###              - given 'S', return 1
###              - given 'R', return 2
###              - given 'w', return 0
s = "RBS, Rutgers"
c = 'w'

def count(s,c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count

print(count(s,c))