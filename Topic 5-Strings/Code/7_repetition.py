def count(s,c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count

def find_repetition(word):
    # 1. ignore cases,
    word = word.upper()

    # 2. count the times each letter appears
    for i in word:
        if count(word, i)>1:
            return True
    
    return False  

word = "rbss"
print(find_repetition(word))