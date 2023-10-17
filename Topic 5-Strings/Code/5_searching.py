# find out whether there is a particular charactor in a string
## if there is, print the index. 
## If there are more than one this charactor, print the first index
## If there is not, print -1
## for example:
#### "RBS Rutgers", return 5 if searching 'u' 
####                return 0 if searching 'R' 
####                return -1 if searching 'w'

## --- method 2 ---
def find_string(s,c):
    # s - a string; c - charactor
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i
            break
    return index

s = 'RBS Rutgers'
c = 's' 

print(find_string(s, c))



## --- method 1 ---
# for i in range(len(s)):
#     if s[i] == c:
#         print(i)
#         break
#     elif i==len(s)-1:
#             print(-1)
    
