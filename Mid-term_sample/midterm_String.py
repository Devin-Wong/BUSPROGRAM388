
def main():
    s = get_string()
    c = 'W'
    index = find_char(s, c)

    if index == -1:
        print(f'There is no {c} in {s}.')
    else:
        print(f'The index of {c} in {s} is {index}.')    

def get_string():
    s = input("Please input a string: ").strip()
    return s

def find_char(s,c):
    # s - a string; c - charactor
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i
            break
    return index

main()