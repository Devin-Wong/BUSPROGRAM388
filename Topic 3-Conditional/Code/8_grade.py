x = int(input("Please input a score: "))

if 0<=x<=100:    # x>=0 and x<=100:    
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
else:
    print("Please input a score within 0 - 100!") 

    
# if x>100 or x<0:
#     print("Please input a score within 0 - 100!") 
# elif x>=90:
#     print("A")
# elif x>=80:
#     print("B")    
# elif x>=70:
#     print("C")    
# elif x>=60:
#     print("D")    
# else:
#     print("F")    
    