# ask user to input name, i.e., first name, then last name
name =  input("Input first name, then last name: ").strip().title()

# split the name into two parts: (1) first name, (2) last name
x = name.split()

# print out
print(f"First name: {x[0]}")
print(f"Last name: {x[1]}")
