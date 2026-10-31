a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
    print("Floor Division =", a // b)
    print("Modulus =", a % b)
else:
    print("Division is not possible")
    print("Floor Division is not possible")
    print("Modulus is not possible")

print("Exponentiation =", a ** b)
