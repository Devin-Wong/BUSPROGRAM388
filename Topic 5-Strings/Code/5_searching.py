# find out whether there is a particular charactor in a string
## if there is, print the index. 
## If there are more than one this charactor, print the first index
## If there is not, print -1
## for example:
#### "RBS Rutgers", return 5 if searching 'u' 
####                return 0 if searching 'R' 
####                return -1 if searching 'w'
s = 'RBS Rutgers'
c = 't' 
for i in range(len(s)):
    if s[i] == c:
        print(i)
        break
    elif i==len(s)-1:
            print(-1)
    
