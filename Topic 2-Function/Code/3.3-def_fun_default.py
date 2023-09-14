def hello(name, greeting="Hello "):
    print(greeting, end="")
    print(name)

name_1 = "Jin"
hello(name_1, "Hi, ")

name_2 = "Neil"
greeting = "Good, "
hello(name_2, greeting="Hi, ")

name_3 = "Mark"
hello(name_3)