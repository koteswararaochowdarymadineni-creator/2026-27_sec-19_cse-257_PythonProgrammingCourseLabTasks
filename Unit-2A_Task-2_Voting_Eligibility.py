age =int(input("Enter your age :"))
if age >=18:
    print("You are eligible to vote.")
elif age<18:
    print("Your are not eligible to vote age are not required.")
elif age<0:
    print("You have not born yet")

else:
    print("You have enter a valid age")