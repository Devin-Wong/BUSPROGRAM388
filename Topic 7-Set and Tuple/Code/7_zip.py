cities = ['Piscataway', 'Highland Park', 'Flagtown']
zipcodes = ['08854', '08904', '08821'] 
counties = ['Middlesex', 'Middlesex', 'Somerset']

# print(list(zip(counties, cities, zipcodes)))

for pair in zip(counties, cities, zipcodes):
    print(pair)

