def summarize_data(l):
    minimum = min(l)
    mean = sum(l)/len(l)
    maximum = max(l)
    return minimum, mean, maximum

l = [1, 2, 5]

minimum, mean, maximum = summarize_data(l)

print(minimum)
print(mean)
print(maximum)
