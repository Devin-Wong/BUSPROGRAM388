cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTOWN']
zipcodes = ['08854', '08940', '08821']

# town name, which we would like to check its zipcode
town = "FLAGTOWN"

## --- method 2: use dictionary ---------
d = dict(zip(cities, zipcodes))
print(d)

print(d[town])

# ## --- method 1: use tuple  --------
# l_tuple = list(zip(cities, zipcodes))
# # print(l_tuple)
# for nm, zipcode in l_tuple:
#     if nm == town:
#         print(zipcode)

