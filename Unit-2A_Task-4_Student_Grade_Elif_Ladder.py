#assign a letter grades A/B/C/:
marks =int(input("Enter a marks:"))
if marks==100:
    print("You have got a A+ grade.")
elif marks<90 and marks>80:
    print(f"you have grade A:(marks ={marks})")
elif marks<80 and marks>70:
    print(f"you have grade B:(marks ={marks})")
elif marks<70 and marks>60:
    print(f"you have grade C:(marks ={marks})")
else:
    print("Invalid grade. (Please enter a grade between 0 and 100)")