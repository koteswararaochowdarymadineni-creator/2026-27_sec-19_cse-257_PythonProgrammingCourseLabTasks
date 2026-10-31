p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in years: "))

si = (p * r * t) / 100
amount = p + si

print("Simple Interest =", si)
print("Total Amount =", amount)
