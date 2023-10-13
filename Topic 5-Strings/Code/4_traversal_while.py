s = "Hello"

##------- 1. print the letter forwards ----
# i = 0
# while i<len(s):   # condition?
#     letter = s[i]
#     print(letter)
#     i = i + 1             # ???

## ---- 2. print the letter backward  ----
#### first method
# i = 0
# while i<len(s):   # condition?
#     letter = s[len(s)-i-1]
#     print(letter)
#     i = i + 1             # ???
#### second method
i = 4
while i>=0:   # condition?
    letter = s[i]
    print(letter)
    i = i - 1             # ???

## expected output
# o
# l
# l
# e
# H                 