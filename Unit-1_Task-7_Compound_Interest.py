p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in years: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", round(ci, 2))
print("Total Amount =", round(amount, 2))
