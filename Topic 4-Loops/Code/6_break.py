## ---- method 1 ------
# while True:
#     x = int(input("Please input a score (0-100): "))
#     if 0<=x<=100:
#         break

## ---- method 2  ------
bl = True
while bl:
    x = int(input("Please input a score (0-100): "))
    if 0<=x<=100:
        bl = False
    
if x>=90:
    print("A")
elif x>=80:
    print("B")    
elif x>=70:
    print("C")    
elif x>=60:
    print("D")    
else:
    print("F")    
