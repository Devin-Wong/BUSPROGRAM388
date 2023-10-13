s = "Hello"
### ------ print letters forward  -------
## method - 1
# for i in s:
#     print(i)

## method - 2
# for i in range(len(s)):
#     print(s[i])

### ------ print letters backward  -------    
s = "Hello"
for i in range(len(s)):
    print(s[len(s)-i-1])
    
