l = [[1, 2], [3], [4, 5, 6]]

def nested_sum(l):
    s = 0 
    for i in l:
        # print(i)
        for j in i:
            s += j
        # print(s)
    return s      

print(nested_sum(l))
