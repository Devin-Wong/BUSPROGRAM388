
def main():
    score = get_score()
    grade = give_grade(score)
    print(f"Score: {score}, Letter grade: {grade}")

def get_score():
    n = int(input("Please input a score (0-100): "))
    return n

def give_grade(x):

    if 0<=x<=100: 
        if x>=90:
            return "A"
        elif x>=85:
            return "B+"    
        elif x>=80:
            return "B"
        elif x>=75:
            return "C+"
        elif x>=70:
            return "C"
        elif x>=60:
            return "D"    
        else:
            return "F"
    else: ## This else statement is not a must.
        print("Please input a score within 0 - 100!") 


main()


