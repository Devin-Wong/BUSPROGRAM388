# create a function, given an address, print streee, city, state,  and zipcode.
## For example: given "100 Rockafeller Road, Piscataway, NJ 08854", it prints: 
###    Street: 100 Rockafeller Road
###    City: Piscataway
###    State: NJ
###    Zipcode: 08854

def address_split(s):
    l = s.split(', ')

    print(f"Street: {l[0]}")
    print(f"City: {l[1]}")
    print(f"State: {l[2][:2]}")
    print(f"Zipcode: {l[2][3:]}")

s = "100 Rockafeller Road, Piscataway, NJ 08854"
address_split(s)





