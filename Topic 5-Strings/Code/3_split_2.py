# ask user to input name, i.e., last name, first name
name = input("Input first name, then last name (e.g., Wang, Jin): ").strip().title()

# split the name into two parts: (1) first name, (2) last name
x = name.split(',')
# print(x)

# print out
print(f"First name: {x[1].strip()}")
print(f"Last name: {x[0].strip()}")
