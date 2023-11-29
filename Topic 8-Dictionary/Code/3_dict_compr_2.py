names = ['Jack', 'Mark', 'Mary', 'Jenny']
ages = [22, 18, 21, 17]

d = {
    names[i]: ages[i] for i in range(len(names)) if ages[i] > 20
}
print(d)

# d = dict(zip(names, ages))
# print(d)