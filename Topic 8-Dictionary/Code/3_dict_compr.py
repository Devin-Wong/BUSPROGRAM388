cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTOWN']
zipcodes = ['08854', '08940', '08821']

# town name, which we would like to check its zipcode
town = "FLAGTOWN"

## --- use comprehension to create dictionary from lists
d = {
    cities[i]: zipcodes[i] for i in range(len(cities))
}

print(d)

# ## --- use dict(zip()) to create dictionary from lists
# d = dict(zip(cities, zipcodes))
# print(d)