def countdown(n):
    if n<=0:
        print("Let's go!!!")
    else:
        print(n)   
        countdown(n-1)

countdown(5)
